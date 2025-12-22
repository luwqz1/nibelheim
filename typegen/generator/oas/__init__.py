import types
import typing

import typegen.generator.oas.v3 as oas3

OAS: typing.Final = types.MappingProxyType(
    mapping={
        oas3.VERSION_MAJOR: oas3.OAS,
    },
)


__all__ = ("OAS",)
