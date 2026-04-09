import logging
import pathlib
import sys

import wreq.blocking as wreq
from packaging.version import Version
from retcon.generators.python import PythonGenerator
from retcon.openapi.parser import decode_openapi_document
from retcon.schema.enums import Enum, EnumValue
from retcon.schema.graph import APISchema
from retcon.schema.nodes import Node
from retcon.schema.objects import Field, Model
from retcon.schema.paths import Endpoint, NamedResponse, Operation, Parameter, RequestBody, Response
from retcon.schema.pipeline import run_generation_pipeline
from retcon.schema.types import ArrayType, EnumRef, MapType, TypeRef, UnionType
from retcon.schema.webhook import Webhook

from nibel.__meta__ import __remnawave__
from typegen.nicificated_schema import EnumSchema, NicificatedSchema, read_schema, write_schema

LOG = logging.getLogger(__name__)


def generate_remnawave(
    workdir: pathlib.Path,
    *,
    nicificated_schema_path: pathlib.Path | None = None,
) -> int:
    handler = logging.StreamHandler(sys.stderr)
    LOG.addHandler(handler)
    handler.setFormatter(logging.Formatter("{levelname: <8} | {asctime} | {funcName} > {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S"))

    schema_path = nicificated_schema_path or pathlib.Path(__file__).with_name("nicificated_schema.yaml")
    nicificated_schema = read_schema(schema_path)

    response = wreq.get(nicificated_schema.remnawave.schema_url)
    response.raise_for_status()

    document = decode_openapi_document(response.bytes(), nicificated_schema.remnawave.schema_document_type)

    if Version(document.info.version) == Version(__remnawave__):
        return 3

    result = run_generation_pipeline(
        document=document,
        document_type=nicificated_schema.remnawave.schema_document_type,
        generator=RemnawaveGenerator(nicificated_schema, schema_path=schema_path),
    )

    workdir.mkdir(parents=True, exist_ok=True)

    for filename, content in result.files.items():
        file = workdir / filename
        file.touch(exist_ok=True)
        file.write_text(content)

    return 0


class RemnawaveGenerator(PythonGenerator):
    def __init__(
        self,
        nicificated_schema: NicificatedSchema,
        *,
        schema_path: pathlib.Path | None = None,
    ) -> None:
        super().__init__(fmt=True, module_name="remnawave")

        self.nicificated_schema = nicificated_schema
        self.schema_path = schema_path or pathlib.Path(__file__).with_name("nicificated_schema.yaml")
        self._nicificated_enum_by_name = {enum_schema.name: enum_schema for enum_schema in self.nicificated_schema.schema.enums.values()}

    @staticmethod
    def _enum_values_set(enum: Enum | EnumSchema) -> set[str | int | float | bool]:
        if isinstance(enum, Enum):
            return {value.value for value in enum.values}
        return set(enum.values)

    @staticmethod
    def _enum_value_name_map(enum_schema: EnumSchema) -> dict[str | int | float, str]:
        return dict(zip(enum_schema.values, enum_schema.members, strict=False))

    def _find_matching_enum_key(self, enum: Enum) -> str | None:
        enum_values = self._enum_values_set(enum)
        exact: list[tuple[str, EnumSchema]] = []
        supersets: list[tuple[str, EnumSchema]] = []
        expandables: list[tuple[str, EnumSchema]] = []

        for enum_key, enum_schema in self.nicificated_schema.schema.enums.items():
            known_values = set(enum_schema.values)

            if enum_values == known_values:
                exact.append((enum_key, enum_schema))
            elif enum_values.issubset(known_values):
                supersets.append((enum_key, enum_schema))
            elif known_values and known_values.issubset(enum_values):
                expandables.append((enum_key, enum_schema))

        def choose(
            candidates: list[tuple[str, EnumSchema]],
            *,
            prefer_smallest: bool,
        ) -> str | None:
            if not candidates:
                return None

            by_name = [enum_key for enum_key, enum_schema in candidates if enum_schema.name == enum.name]
            if len(by_name) == 1:
                return by_name[0]
            if len(by_name) > 1:
                LOG.warning("Multiple nicificated enums matched `%s` by name: %s", enum.name, ", ".join(sorted(by_name)))
                return None

            ordered = sorted(
                candidates,
                key=lambda item: (len(item[1].values), item[1].name),
                reverse=not prefer_smallest,
            )
            best_key, best_schema = ordered[0]
            best_size = len(best_schema.values)
            same_size = [enum_key for enum_key, enum_schema in ordered if len(enum_schema.values) == best_size]

            if len(same_size) > 1:
                LOG.warning(
                    "Ambiguous nicificated enum match for `%s` with values %s: %s",
                    enum.name,
                    sorted(enum_values, key=repr),
                    ", ".join(sorted(same_size)),
                )
                return None

            return best_key

        return choose(exact, prefer_smallest=True) or choose(supersets, prefer_smallest=True) or choose(expandables, prefer_smallest=False)

    def _sync_enum_into_nicificated_schema(self, enum_key: str, enum: Enum) -> bool:
        enum_schema = self.nicificated_schema.schema.enums[enum_key]
        known_value_names = self._enum_value_name_map(enum_schema)
        updated = False

        if enum_schema.description is None and enum.description:
            enum_schema.description = enum.description
            updated = True

        for enum_value in enum.values:
            if enum_value.value in known_value_names:
                continue

            member_name = enum_value.name
            if member_name in enum_schema.members:
                base_name = member_name
                counter = 2
                while member_name in enum_schema.members:
                    member_name = f"{base_name}_{counter}"
                    counter += 1

            enum_schema.members.append(member_name)
            enum_schema.values.append(enum_value.value)
            updated = True
            LOG.info("Added new enum member `%s.%s = %r` to nicificated schema", enum_schema.name, member_name, enum_value.value)

        if updated:
            self._nicificated_enum_by_name[enum_schema.name] = enum_schema

        return updated

    def _build_enum_from_nicificated_schema(self, enum_key: str) -> Enum:
        enum_schema = self.nicificated_schema.schema.enums[enum_key]
        return Enum(
            name=enum_schema.name,
            description=enum_schema.description,
            values=[EnumValue(name=member, value=value) for member, value in zip(enum_schema.members, enum_schema.values, strict=False)],
        )

    def _rewrite_enum_ref(self, type_ref: TypeRef, enum_name_map: dict[str, str]) -> TypeRef:
        if isinstance(type_ref, EnumRef):
            return EnumRef(
                name=enum_name_map.get(type_ref.name, type_ref.name),
                nullable=type_ref.nullable,
                constraints=type_ref.constraints,
            )

        if isinstance(type_ref, ArrayType):
            return ArrayType(
                item_type=self._rewrite_enum_ref(type_ref.item_type, enum_name_map),
                nullable=type_ref.nullable,
                constraints=type_ref.constraints,
            )

        if isinstance(type_ref, MapType):
            return MapType(
                value_type=self._rewrite_enum_ref(type_ref.value_type, enum_name_map),
                nullable=type_ref.nullable,
                constraints=type_ref.constraints,
            )

        if isinstance(type_ref, UnionType):
            return UnionType(
                variants=[self._rewrite_enum_ref(variant, enum_name_map) for variant in type_ref.variants],
                nullable=type_ref.nullable,
                constraints=type_ref.constraints,
            )

        return type_ref

    def _rewrite_model_enums(self, model: Model, enum_name_map: dict[str, str]) -> Model:
        return Model(
            name=model.name,
            fields=[
                Field(
                    name=field.name,
                    type=self._rewrite_enum_ref(field.type, enum_name_map),
                    required=field.required,
                    description=field.description,
                    default=field.default,
                    deprecated=field.deprecated,
                )
                for field in model.fields
            ],
            description=model.description,
            deprecated=model.deprecated,
        )

    def _rewrite_operation_enums(self, op: Operation, enum_name_map: dict[str, str]) -> Operation:
        return Operation(
            method=op.method,
            path=op.path,
            operation_id=op.operation_id,
            summary=op.summary,
            description=op.description,
            tags=op.tags,
            parameters=[
                Parameter(
                    name=param.name,
                    location=param.location,
                    type=self._rewrite_enum_ref(param.type, enum_name_map),
                    required=param.required,
                    description=param.description,
                    deprecated=param.deprecated,
                )
                for param in op.parameters
            ],
            request_body=(
                None
                if op.request_body is None
                else RequestBody(
                    content_type=op.request_body.content_type,
                    type=self._rewrite_enum_ref(op.request_body.type, enum_name_map),
                    required=op.request_body.required,
                    description=op.request_body.description,
                )
            ),
            responses=[
                Response(
                    status_code=response.status_code,
                    description=response.description,
                    content={content_type: self._rewrite_enum_ref(type_ref, enum_name_map) for content_type, type_ref in response.content.items()},
                    component_response_ref=response.component_response_ref,
                )
                for response in op.responses
            ],
            deprecated=op.deprecated,
            security_requirements=op.security_requirements,
        )

    def _harmonize_schema_enums(self, schema: APISchema) -> APISchema:
        if not schema.enums:
            return schema

        enum_name_map: dict[str, str] = {}
        rewritten_enums: list[Enum] = []
        matched_names: set[str] = set()
        schema_updated = False

        for enum in schema.enums:
            enum_key = self._find_matching_enum_key(enum)
            if enum_key is None:
                LOG.warning(
                    "No nicificated enum match found for `%s` with values %s",
                    enum.name,
                    [enum_value.value for enum_value in enum.values],
                )
                enum_name_map[enum.name] = enum.name
                rewritten_enums.append(enum)
                continue

            if self._sync_enum_into_nicificated_schema(enum_key, enum):
                schema_updated = True

            canonical_enum = self._build_enum_from_nicificated_schema(enum_key)
            enum_name_map[enum.name] = canonical_enum.name

            if canonical_enum.name not in matched_names:
                rewritten_enums.append(canonical_enum)
                matched_names.add(canonical_enum.name)

        if schema_updated:
            write_schema(self.nicificated_schema, self.schema_path)

        def rewrite_custom_node(node: Node) -> Node:
            if isinstance(node, Model):
                return self._rewrite_model_enums(node, enum_name_map)

            if isinstance(node, Enum):
                enum_key = self._find_matching_enum_key(node)
                if enum_key is not None:
                    return self._build_enum_from_nicificated_schema(enum_key)

            return node

        return APISchema(
            title=schema.title,
            version=schema.version,
            description=schema.description,
            servers=schema.servers,
            models=[self._rewrite_model_enums(model, enum_name_map) for model in schema.models],
            enums=rewritten_enums,
            endpoints=[
                Endpoint(
                    path=endpoint.path,
                    operations=[self._rewrite_operation_enums(op, enum_name_map) for op in endpoint.operations],
                    description=endpoint.description,
                )
                for endpoint in schema.endpoints
            ],
            webhooks=[
                Webhook(
                    name=webhook.name,
                    operations=[self._rewrite_operation_enums(op, enum_name_map) for op in webhook.operations],
                    description=webhook.description,
                )
                for webhook in schema.webhooks
            ],
            named_responses=[
                NamedResponse(
                    name=response.name,
                    status_codes=response.status_codes,
                    description=response.description,
                    content={content_type: self._rewrite_enum_ref(type_ref, enum_name_map) for content_type, type_ref in response.content.items()},
                    schema_ref=response.schema_ref,
                )
                for response in schema.named_responses
            ],
            security_schemes=schema.security_schemes,
            custom_nodes=[rewrite_custom_node(node) for node in schema.custom_nodes],
        )

    def _render_custom_enum(self, enum: Enum) -> str:
        return self._render_enum(enum)

    def _render_enum(self, enum: Enum) -> str:
        enum_schema = self._nicificated_enum_by_name.get(enum.name)
        lines = [f"class {enum.name}(msgspex.{self._enum_base_class(enum)}, metaclass=msgspex.BaseEnumMeta):"]

        if enum.description:
            lines.append(f'    """{enum.description}"""')
            lines.append("")

        if not enum.values:
            lines.append("    pass")
            return "\n".join(lines)

        for enum_value in enum.values:
            lines.append(f"    {enum_value.name} = {self._dquote_repr(enum_value.value)}")

            if enum_schema is not None:
                member_description = enum_schema.member_descriptions.get(enum_value.name)

                if member_description:
                    lines.append(f'    """{member_description}"""')
                    lines.append("")

        return "\n".join(lines).rstrip()

    def generate(self, schema: APISchema) -> dict[str, str]:
        return super().generate(self._harmonize_schema_enums(schema))

    def generate_custom_node(self, node: Node) -> str | None:
        match node:
            case Enum():
                return self._render_custom_enum(node)
            case _:
                return None


__all__ = ("RemnawaveGenerator", "generate_remnawave")
