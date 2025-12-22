import pathlib
import typing

from jinja2 import Environment
from packaging.version import parse

from typegen.generator.abc import ABCGenerator, Context
from typegen.schema.oas.v3.oas_3_0_0.remna import RemnaAPI

VERSION: typing.Final = parse("3.0.0")


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
        pass


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
