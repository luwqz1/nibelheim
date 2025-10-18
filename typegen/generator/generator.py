import abc
import pathlib
import typing

import jinja2
import msgspec
import niquests
from packaging.version import parse

from nibel.logger import get_logger
from src.__meta__ import __remnawave_api__
from typegen.model import decode_hook
from typegen.schema.remna import OAS, RemnaAPI

type Context = dict[str, typing.Any]

REMNA_API_VERSION: typing.Final = parse(__remnawave_api__)
TYPEGEN_OAS: typing.Final = parse("3.1.1")
REMNA_OPENAPI_URL: typing.Final = "https://cdn.remna.st/docs/openapi.json"
API_MAP_TYPES: typing.Final = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "dict",
    "array": "list",
}
API_MAP_FORMATS: typing.Final = {
    "date-time": "datetime",
    "timestamp": "datetime",
    "uuid": "UUID",
}

logger = get_logger(__name__)


class ABCGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(
        self,
        work_path: pathlib.Path,
        remna_api: RemnaAPI,
        jinja_env: jinja2.Environment,
        context: Context,
    ) -> None:
        pass


def generate(
    work_path: pathlib.Path,
    objects_generator: ABCGenerator | None = None,
    paths_generator: ABCGenerator | None = None,
    errors_generator: ABCGenerator | None = None,
    enums_generator: ABCGenerator | None = None,
    jinja_loader: jinja2.FileSystemLoader | None = None,
) -> None:
    if not any((objects_generator, paths_generator, errors_generator, enums_generator)):
        logger.error("No generators provided.")
        return

    raw_response = niquests.get(url=REMNA_OPENAPI_URL).content  # type: ignore
    if not raw_response:
        logger.error("Failed to fetch Remnawave API schema.")
        return

    remna_oas = msgspec.json.decode(raw_response, type=OAS)
    if remna_oas.version != TYPEGEN_OAS:
        logger.critical(
            "Remnawave Open API Schema version `{}` is not supported. Generator supported version: `{}`.",
            remna_oas.version,
            TYPEGEN_OAS,
        )
        return

    remna_api = msgspec.json.decode(raw_response, type=RemnaAPI, dec_hook=decode_hook)
    if remna_api.version == REMNA_API_VERSION:
        logger.info("Remnawave API version `{}` is up to date. Skipping generation.", remna_api.version)
        return

    jinja_env = jinja2.Environment(
        loader=jinja_loader or jinja2.FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    context: Context = dict()

    logger.info("New Remnawave API version `{}` detected. Generating API...", remna_api.version)

    if objects_generator:
        objects_generator.generate(work_path, remna_api, jinja_env, context)

    if paths_generator:
        paths_generator.generate(work_path, remna_api, jinja_env, context)

    if errors_generator:
        errors_generator.generate(work_path, remna_api, jinja_env, context)

    if enums_generator:
        enums_generator.generate(work_path, remna_api, jinja_env, context)


__all__ = ("generate",)
