import types
import typing

from typegen.schema.oas import v3

OAS: typing.Final = types.MappingProxyType(
    mapping={
        v3.MAJOR_VERSION: v3.OAS,
    },
)

__all__ = ("OAS",)
