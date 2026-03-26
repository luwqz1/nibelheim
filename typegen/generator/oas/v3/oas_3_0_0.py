import pathlib
import sys
import typing
from collections import deque

import msgspec
import niquests
from jinja2 import Environment
from packaging.version import parse
from typegen.generator.abc import ABCGenerator, Context
from typegen.generator.utils import makesafe_name_from_enum_value

from nibel.logger import get_logger
from typegen.cfg.config import Config
from typegen.generator.external.aes import generate_aes_to_oas_enum
from typegen.schema.external.aes import RemnawaveAES
from typegen.schema.oas.v3.oas_3_0_0.properties import (
    ArrayPropertySchema,
    BooleanPropertySchema,
    IntegerPropertySchema,
    NumberPropertySchema,
    ObjectPropertySchema,
    Property,
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
    def generate_enumerations_from_props(
        api: RemnaAPI,
        config: Config,
        context: Context,
        props: list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]],
    ) -> list[tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]]:
        LOG.info("Generating enumerations from properties...")

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
        LOG.info("{} enumerations from properties generated successfully!", len(enums))
        return enums

    @staticmethod
    def generate_aes_enum(
        api: RemnaAPI,
        config: Config,
    ) -> tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]:
        LOG.info("Generating `{}` enum by an external AES schema...", "ErrorCode")

        try:
            LOG.debug("Downloading Remnawave AES schema from `{!s}`...", config.remnawave.aes_url)
            response = niquests.get(config.remnawave.aes_url).content  # type: ignore
        except Exception as e:
            LOG.error("Failed to download Remnawave AES schema with error: '{!s}'", e)
            sys.exit(-1)

        if not response:
            LOG.error("Failed to download Remnawave AES schema.")
            sys.exit(-1)

        LOG.debug("Remnawave AES schema downloaded successfully, decoding...")

        try:
            aes_schema = msgspec.json.decode(response, type=RemnawaveAES)
        except Exception as e:
            LOG.error("Failed to decode Remnawave AES schema with error: '{!s}'", e)
            sys.exit(-1)

        LOG.debug("Remnawave AES schema decoded successfully!")

        if api.version != aes_schema.remna_version:
            LOG.error("Remnawave API version `{}` does not match AES schema version `{}`.", api.version, aes_schema.remnawave)
            sys.exit(-1)

        LOG.debug("Generating from `{}` schema to `{}` schema", "AES", "OAS")
        return generate_aes_to_oas_enum(aes_schema)

    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        return
        LOG.info("Generating enumerations...")

        config: Config = context["config"]
        enums_template = environment.get_template("enums.j2")
        enums_path = workdir / "enums.py"

        props = [
            *self.get_enums_props_from_components(api),
            *self.get_enums_props_from_paths(api),
        ]
        enums = self.generate_enumerations_from_props(api, config, context, props)

        LOG.info("Rendering {} enumerations to `{}` file...", len(enums), enums_path)
        enums_path.write_text(
            data=enums_template.render(enums=sorted(enums, key=lambda x: x[0])),
            encoding="UTF-8",
        )
        LOG.info("{} enumerations rendered to `{}` file successfully!", len(enums), enums_path)
        print("\n", file=sys.stderr)


class ErrorsGenerator(ABCGenerator):
    @staticmethod
    def generate_errors_classes_components(
        schema_errors: dict[str, dict[str, Property]],
    ) -> dict[str, dict[str, Property]]:
        classes: dict[str, typing.Any] = {}

        for error_name, error_properties in schema_errors.items():
            stack = deque(((error_name, tuple(error_properties.items())),))

            while stack:
                class_name, properties = stack.pop()
                props: dict[str, Property] = {}

                for property_name, property_value in properties:
                    if isinstance(property_value, ArrayPropertySchema) and property_value.items.type == PropertyType.OBJECT:
                        if property_name != "errors":
                            LOG.warning(
                                "Currently, only `{}` property is supported for array of errors in error responses, got `{}`, just skipping...",
                                "errors",
                                property_name,
                            )
                            continue

                        new_class_name = class_name.replace("Response", "")
                        stack.append((new_class_name, (("", property_value.items),)))
                        property_value.ref = f"#/paths/errors/{new_class_name}"
                        props[property_name] = property_value
                        continue

                    if not isinstance(property_value, ArrayPropertySchema) and property_value.properties:
                        stack.append((class_name, tuple(property_value.properties.items())))
                        property_value.ref = f"#/paths/errors/{class_name}"
                        props[property_name] = property_value
                        continue

                    props[property_name] = property_value

                classes[class_name] = props

        return classes

    @staticmethod
    def get_schema_errors(api: RemnaAPI) -> dict[str, dict[str, Property]]:
        schema_errors: dict[str, dict[str, Property]] = {}

        for path in api.paths.values():
            for method in path.methods.values():
                if not method.responses:
                    continue

                for status_code, response in method.responses.items():
                    if status_code == "default" or int(status_code) < 400 or not response.content:
                        continue

                    if not response.content.application_json:
                        LOG.warning(
                            "Currently, only `{}` content type is supported for error responses, skipping...",
                            "application/json",
                        )
                        continue

                    error_schema = response.content.application_json.schema
                    if error_schema.type != "object" or not error_schema.properties:
                        continue

                    error_class_name = "APIResponse"
                    error_class_name += "".join(x.capitalize() for x in response.description.split()).strip(".").replace("-", "")

                    if not error_class_name.endswith("Error"):
                        error_class_name += "Error"

                    schema_errors.setdefault(error_class_name, error_schema.properties)

        return schema_errors

    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        LOG.info("Generating errors...")

        errors_path = workdir / "errors.py"
        errors_template = environment.get_template("errors.j2")

        schema_errors = self.get_schema_errors(api)
        errors_classes = self.generate_errors_classes_components(schema_errors)

        LOG.info("Rendering {} errors classes to `{}` file...", len(errors_classes), errors_path)
        errors_path.write_text(
            data=errors_template.render(errors_classes=errors_classes),
            encoding="UTF-8",
        )
        LOG.info("{} errors classes rendered to `{}` file successfully!", len(errors_classes), errors_path)


__all__ = (
    "VERSION",
    "ArrayPropertySchema",
    "BooleanPropertySchema",
    "EnumsGenerator",
    "ErrorsGenerator",
    "IntegerPropertySchema",
    "NumberPropertySchema",
    "ObjectPropertySchema",
    "ObjectsGenerator",
    "Property",
    "StringPropertySchema",
)
