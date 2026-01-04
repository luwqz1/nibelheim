import pathlib
import sys
import typing
from collections import deque

import msgspec
import niquests
from jinja2 import Environment
from packaging.version import parse

from nibel.logger import get_logger
from typegen.cfg.config import Config
from typegen.generator.abc import ABCGenerator, Context
from typegen.generator.external.aes import generate_aes_to_oas_enum
from typegen.generator.utils import makesafe_name_from_enum_value
from typegen.schema.external.aes import RemnawaveAES
from typegen.schema.oas.v3.oas_3_0_0.properties import (
    ArrayPropertySchema,
    IntegerPropertySchema,
    NumberPropertySchema,
    ObjectPropertySchema,
    PropertyType,
    StringPropertySchema,
)
from typegen.schema.oas.v3.oas_3_0_0.remna import RemnaAPI

VERSION: typing.Final = parse("3.0.0")
LOG: typing.Final = get_logger(__name__)


class ObjectsGenerator(ABCGenerator):
    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        pass


class EnumsGenerator(ABCGenerator):
    @staticmethod
    def get_enums_props_from_components(api: RemnaAPI) -> list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]]:
        props: list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]] = []

        for component in api.components.schemas.values():
            if component.type != "object":
                continue

            stack = deque(
                ((typing.cast("str | None", None), tuple(component.properties.items())),),
            )

            while stack:
                component_name, properties = stack.pop()

                for name, prop in properties:
                    match prop:
                        case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema():
                            if prop.enum_values:
                                props.append(((component_name if component_name else "") + (name[0].upper() + name[1:] if component_name else name), prop))
                            elif prop.properties:
                                stack.append((name, tuple(prop.properties.items())))
                        case ObjectPropertySchema() if prop.properties:
                            stack.append((name, tuple(prop.properties.items())))
                        case ArrayPropertySchema() if prop.items:
                            stack.append((component_name, ((name, prop.items),)))
                        case _:
                            continue

        return props

    @staticmethod
    def get_enums_props_from_paths(api: RemnaAPI) -> list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]]:
        props: list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]] = []

        for method in api.paths.values():
            if method.method is None:
                continue

            for param in method.method.parameters:
                match param.schema:
                    case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema() if param.schema.enum_values:
                        props.append((param.name, param.schema))
                    case _:
                        continue

        return props

    @staticmethod
    def generate_enum_enumerations(
        api: RemnaAPI,
        config: Config,
        context: Context,
        props: list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]],
    ) -> list[tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]]:
        enums: list[tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]] = []
        enums_dicts: dict[str, dict[str, typing.Any]] = {}
        enums_descriptions: dict[str, str] = {}

        for prop_name, prop in props:
            if prop_name in config.generator.enums.custom_enums:
                enum = config.generator.enums.custom_enums[prop_name]
            elif prop.enum_names and prop.enum_values:
                enum = dict(zip(prop.enum_names, prop.enum_values))
            elif prop.enum_values and prop.type == PropertyType.STRING:
                skip = False

                for enum_name, *_, enum_dict, _ in enums:
                    pname = config.generator.enums.renames.get(prop_name, prop_name)
                    if enum_name == pname and pname not in context.get("enums", {}):
                        if all(x in enum_dict for x in prop.enum_values):
                            context.setdefault("enums", {})[pname] = tuple(map(makesafe_name_from_enum_value, prop.enum_values))
                        else:
                            LOG.warning("Repeated enum values {!r} found with similar name: {!r}", prop.enum_values, prop_name)

                        skip = True
                        break

                if skip:
                    continue

                enum = dict(zip(map(makesafe_name_from_enum_value, prop.enum_values), prop.enum_values))
            else:
                continue

            if prop_name not in enums_dicts:
                is_similar_enum = False

                for enum_dict in enums_dicts.values():
                    if all(x in enum_dict for x in enum.values()):
                        is_similar_enum = True
                        break

                if is_similar_enum:
                    continue

                enums_dicts[prop_name] = enum

                name = config.generator.enums.renames.get(prop_name, prop_name)
                prop_description = config.generator.enums.class_descriptions.get(name, prop.desc)

                if prop_description and name not in enums_descriptions:
                    if isinstance(prop_description, dict):
                        if name not in config.generator.enums.enumerations_descriptions and "markdownEnumDescriptions" in prop_description:
                            config.generator.enums.enumerations_descriptions[name] = dict(zip(enum.keys(), prop_description["markdownEnumDescriptions"]))

                        prop_description = prop_description.get("title", prop_description.get("markdownDescription", None))

                    if isinstance(prop_description, str):
                        enums_descriptions[name] = prop_description

                enums.append(
                    (
                        name,
                        enums_descriptions.get(name),
                        prop.type.value,
                        enum,
                        config.generator.enums.enumerations_descriptions.get(name),
                    ),
                )
            else:
                enums_dicts[prop_name].update(enum)

        enums.append(EnumsGenerator.generate_aes_enum(api, config))
        return enums

    @staticmethod
    def generate_aes_enum(
        api: RemnaAPI,
        config: Config,
    ) -> tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]:
        response = niquests.get(config.remnawave.aes_url).content  # type: ignore
        if not response:
            LOG.error("Failed to download Remnawave AES schema.")
            sys.exit(-1)

        aes_schema = msgspec.json.decode(response, type=RemnawaveAES)
        if api.version != aes_schema.remna_version:
            LOG.error("Remnawave API version `{}` does not match AES schema version `{}`.", api.version, aes_schema.remnawave)
            sys.exit(-1)

        return generate_aes_to_oas_enum(aes_schema)

    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        LOG.info("Generating enums...")

        config: Config = context["config"]
        enums_template = environment.get_template("enums.j2")
        enums_path = workdir / "enums.py"

        props = [
            *self.get_enums_props_from_components(api),
            *self.get_enums_props_from_paths(api),
        ]
        enums = self.generate_enum_enumerations(api, config, context, props)

        enums_path.write_text(
            data=enums_template.render(enums=sorted(enums, key=lambda x: x[0])),
            encoding="UTF-8",
        )
        LOG.info("{} enums generated successfully!", len(enums))


class ErrorsGenerator(ABCGenerator):
    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        pass


__all__ = ("VERSION", "EnumsGenerator", "ErrorsGenerator", "ObjectsGenerator")
