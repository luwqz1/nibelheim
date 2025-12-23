import pathlib
import typing

from jinja2 import Environment
from packaging.version import parse

from nibel.logger import get_logger
from typegen.cfg.config import Config
from typegen.generator.abc import ABCGenerator, Context
from typegen.schema.oas.v3.oas_3_1_1.components import (
    IntegerPropertySchema,
    NumberPropertySchema,
    StringPropertySchema,
)
from typegen.schema.oas.v3.oas_3_1_1.remna import RemnaAPI

VERSION: typing.Final = parse("3.1.1")
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

        config: Config = context["config"]
        enums: list[tuple[str, str | None, str, dict[str, typing.Any], dict[str, str] | None]] = []
        enums_dicts: list[dict[str, typing.Any]] = []
        enums_descriptions: dict[str, str] = {}
        enums_template = environment.get_template("enums.j2")
        enums_path = workdir / "enums.py"

        for component in api.components.schemas.values():
            if component.type != "object":
                continue

            for name, prop in component.properties.items():
                match prop:
                    case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema() if prop.enum_names and prop.enum_values:
                        enum = dict(zip(prop.enum_names, prop.enum_values))
                        if enum not in enums_dicts:
                            enums_dicts.append(enum)

                            name = config.generator.enums.renames.get(name, name)
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
                    case _:
                        continue

        enums_path.write_text(enums_template.render(enums=enums), encoding="utf-8")
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
