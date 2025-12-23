import pathlib
import typing

from jinja2 import Environment
from packaging.version import parse

from nibel.logger import get_logger
from typegen.cfg.config import Config
from typegen.generator.abc import ABCGenerator, Context
from typegen.generator.utils import makesafe_name_from_enum_value
from typegen.schema.oas.v3.oas_3_0_0.components import (
    IntegerPropertySchema,
    NumberPropertySchema,
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
    def generate(
        self,
        api: RemnaAPI,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        LOG.info("Generating enums...")

        enums_template = environment.get_template("enums.j2")
        enums_path = workdir / "enums.py"

        config: Config = context["config"]
        enums: list[tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]] = []
        enums_dicts: list[dict[str, typing.Any]] = []
        enums_descriptions: dict[str, str] = {}
        props: list[tuple[str, StringPropertySchema | IntegerPropertySchema | NumberPropertySchema]] = []

        for component in api.components.schemas.values():
            if component.type != "object":
                continue

            for name, prop in component.properties.items():
                match prop:
                    case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema() if prop.enum_values:
                        props.append((name, prop))
                    case _:
                        continue

        for method in api.paths.values():
            if method.method is None:
                continue

            for param in method.method.parameters:
                match param.schema:
                    case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema() if param.schema.enum_values:
                        props.append((param.name, param.schema))
                    case _:
                        continue

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

            if enum not in enums_dicts:
                enums_dicts.append(enum)

                name = config.generator.enums.renames.get(prop_name, prop_name)
                prop_description = config.generator.enums.class_descriptions.get(name, prop.description)

                if prop_description and name not in enums_descriptions:
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

        enums_path.write_text(enums_template.render(enums=sorted(enums, key=lambda x: x[0])), encoding="utf-8")
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
