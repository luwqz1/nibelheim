import typing

import msgspec
import niquests

from typegen.schema.remna import RemnaAPI

TYPEGEN_OPENAPI_VERSION: typing.Final = "3.0.0"
REMNA_OPENAPI_URL: typing.Final = "https://cdn.remna.st/docs/openapi.json"
REMNA_MAP_TYPES: typing.Final = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
}
REMNA_MAP_FORMATS: typing.Final = {
    "date-time": "datetime",
    "uuid": "UUID",
}
REMNA_MAP_METAS: typing.Final = {
    "minLength": "min_length",
    "maxLength": "max_length",
    "pattern": "pattern",
}

raw_response = niquests.get(url=REMNA_OPENAPI_URL).content  # type: ignore
assert raw_response is not None

remna_api = msgspec.json.decode(raw_response, type=RemnaAPI)
