import abc
import typing

import jinja2
import msgspec
import niquests

from typegen.model import decode_hook
from typegen.schema.remna import RemnaAPI

TYPEGEN_OPENAPI_VERSION: typing.Final = "3.0.0"
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


class ABCGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, remna_api: RemnaAPI, jinja_env: jinja2.Environment) -> None:
        pass


def generate(
    objects_generator: ABCGenerator | None = None,
    paths_generator: ABCGenerator | None = None,
    errors_generator: ABCGenerator | None = None,
    enums_generator: ABCGenerator | None = None,
    jinja_loader: jinja2.FileSystemLoader | None = None,
) -> None:
    if not any((objects_generator, paths_generator, errors_generator, enums_generator)):
        raise RuntimeError("No generators provided.")

    raw_response = niquests.get(url=REMNA_OPENAPI_URL).content  # type: ignore

    if not raw_response:
        raise RuntimeError("Failed to fetch Remnawave API schema.")

    remna_api = msgspec.json.decode(raw_response, type=RemnaAPI, dec_hook=decode_hook)
    jinja_env = jinja2.Environment(
        loader=jinja_loader or jinja2.FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if objects_generator:
        objects_generator.generate(remna_api, jinja_env)

    if paths_generator:
        paths_generator.generate(remna_api, jinja_env)

    if errors_generator:
        errors_generator.generate(remna_api, jinja_env)

    if enums_generator:
        enums_generator.generate(remna_api, jinja_env)


__all__ = ("generate",)
