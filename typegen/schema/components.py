import enum
import typing

import msgspec

from typegen.schema.properties import BasePropertySchema, PropertySchema
from typegen.schema.security import SecuritySchemes

type Schemas = dict[str, Component]
type Property = typing.Union[
    StringPropertySchema,
    IntegerPropertySchema,
    NumberPropertySchema,
    BooleanPropertySchema,
    ArrayPropertySchema,
    ObjectPropertySchema,
]


class PropertyType(enum.Enum):
    STRING = "string"
    INTEGER = "integer"
    NUMBER = "number"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"

    def to_str(self) -> str:
        return self.value


class ComponentPropertyTaggedFieldType(msgspec.Struct, tag_field="type"):
    @property
    def type(self) -> PropertyType:
        tag = self.__struct_config__.tag
        return PropertyType.OBJECT if tag is None else PropertyType(tag)


class ComponentPropertySchema(BasePropertySchema, ComponentPropertyTaggedFieldType):
    pass


class StringPropertySchema(ComponentPropertySchema, tag=PropertyType.STRING.to_str()):
    pass


class IntegerPropertySchema(ComponentPropertySchema, tag=PropertyType.INTEGER.to_str()):
    pass


class NumberPropertySchema(ComponentPropertySchema, tag=PropertyType.NUMBER.to_str()):
    pass


class BooleanPropertySchema(ComponentPropertySchema, tag=PropertyType.BOOLEAN.to_str()):
    pass


class ObjectPropertySchema(ComponentPropertyTaggedFieldType, tag_field="type", tag=PropertyType.OBJECT.to_str()):
    additional_properties: PropertySchema | None = msgspec.field(default=None, name="additionalProperties")
    properties: dict[str, Property] | None = msgspec.field(default=None)
    required: list[str] = msgspec.field(default_factory=list)
    nullable: bool | None = msgspec.field(default=None)


class ArrayPropertySchema(ComponentPropertyTaggedFieldType, tag_field="type", tag=PropertyType.ARRAY.to_str()):
    items: Property
    required: list[str] = msgspec.field(default_factory=list)


class Component(msgspec.Struct):
    type: str
    properties: dict[str, Property]
    required: list[str] = msgspec.field(default_factory=list)


class Components(msgspec.Struct):
    schemas: Schemas
    security_schemes: SecuritySchemes = msgspec.field(name="securitySchemes")


__all__ = ("Components",)
