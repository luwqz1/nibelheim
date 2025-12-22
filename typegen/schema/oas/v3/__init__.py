import types
import typing

from typegen.schema.oas.v3 import oas_3_0_0, oas_3_1_1

MAJOR_VERSION: typing.Final = 3
OAS: typing.Final = types.MappingProxyType(
    mapping={
        oas_3_0_0.OAS_3_0_0: oas_3_0_0,
        oas_3_1_1.OAS_3_1_1: oas_3_1_1,
    },
)

__all__ = ("MAJOR_VERSION", "OAS")
