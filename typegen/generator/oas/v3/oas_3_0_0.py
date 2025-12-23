import pathlib
import typing

from jinja2 import Environment
from packaging.version import parse

from nibel.logger import get_logger
from typegen.generator.abc import ABCGenerator, Context
from typegen.schema.oas.v3.oas_3_0_0.components import (
    IntegerPropertySchema,
    NumberPropertySchema,
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

        enums: list[tuple[str, str, dict[str, typing.Any]]] = []
        enums_template = environment.get_template("enums.j2")
        enums_path = workdir / "enums.py"

        for component in api.components.schemas.values():
            if component.type != "object":
                continue

            for name, prop in component.properties.items():
                match prop:
                    case StringPropertySchema() | IntegerPropertySchema() | NumberPropertySchema() if prop.enum_names and prop.enum_values:
                        enum = (name, prop.type.value, dict(zip(prop.enum_names, prop.enum_values)))

                        if enum not in enums:
                            enums.append(enum)
                    case _:
                        continue

        enums_path.write_text(enums_template.render(enums=enums))
        LOG.info(f"{len(enums)} enums generated successfully!")


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
