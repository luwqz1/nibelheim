import typing

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


def get_remna_api() -> RemnaAPI:
    raw_response = niquests.get(url=REMNA_OPENAPI_URL).content  # type: ignore
    assert raw_response is not None, "Failed to fetch Remna API"
    return msgspec.json.decode(raw_response, type=RemnaAPI, dec_hook=decode_hook)


print(get_remna_api())
