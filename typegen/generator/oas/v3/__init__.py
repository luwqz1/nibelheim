import types
import typing

import typegen.generator.oas.v3.oas_3_0_0 as oas300
import typegen.generator.oas.v3.oas_3_1_1 as oas311

VERSION_MAJOR: typing.Final = 3
OAS: typing.Final = types.MappingProxyType(
    mapping={
        oas300.VERSION: (oas300.ObjectsGenerator(), oas300.EnumsGenerator(), oas300.ErrorsGenerator()),
        oas311.VERSION: (oas311.ObjectsGenerator(), oas311.EnumsGenerator(), oas311.ErrorsGenerator()),
    },
)


__all__ = ("OAS", "VERSION_MAJOR")
