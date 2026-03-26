import types
import typing

import typegen.generator.oas.v3.oas_3_0_0 as oas300
import typegen.generator.oas.v3.oas_3_1_1 as oas311

StringPropertySchema = oas300.StringPropertySchema | oas311.StringPropertySchema
IntegerPropertySchema = oas300.IntegerPropertySchema | oas311.IntegerPropertySchema
NumberPropertySchema = oas300.NumberPropertySchema | oas311.NumberPropertySchema
ArrayPropertySchema = oas300.ArrayPropertySchema | oas311.ArrayPropertySchema
BooleanPropertySchema = oas300.BooleanPropertySchema | oas311.BooleanPropertySchema
ObjectPropertySchema = oas300.ObjectPropertySchema | oas311.ObjectPropertySchema
Property = oas300.Property | oas311.Property


VERSION_MAJOR: typing.Final = 3
OAS: typing.Final = types.MappingProxyType(
    mapping={
        oas300.VERSION: (oas300.EnumsGenerator(), oas300.ErrorsGenerator(), oas300.ObjectsGenerator()),
        oas311.VERSION: (oas311.EnumsGenerator(), oas311.ErrorsGenerator(), oas311.ObjectsGenerator()),
    },
)


__all__ = (
    "OAS",
    "VERSION_MAJOR",
    "ArrayPropertySchema",
    "BooleanPropertySchema",
    "IntegerPropertySchema",
    "NumberPropertySchema",
    "ObjectPropertySchema",
    "Property",
    "StringPropertySchema",
)
