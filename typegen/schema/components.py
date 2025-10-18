import enum
import typing

import msgspec

from typegen.model import Model, Union
from typegen.schema.properties import BasePropertySchema, PropertySchema
from typegen.schema.security import SecuritySchemes

type Schemas = dict[str, Component]
type Property = Union[
    StringPropertySchema,
    IntegerPropertySchema,
    NumberPropertySchema,
    BooleanPropertySchema,
    ArrayPropertySchema,
    ObjectPropertySchema,
    DefaultPropertySchema,
]


def get_tag(struct_qualname: str) -> str:
    name = struct_qualname.lower()
    return next(x.value for x in PropertyType if name.startswith(x.value))


class PropertyType(enum.Enum):
    STRING = "string"
    INTEGER = "integer"
    NUMBER = "number"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"


class ComponentPropertyTaggedFieldType(Model, tag_field="type"):
    @property
    def type(self) -> PropertyType:
        tag = self.__struct_config__.tag
        return PropertyType.OBJECT if tag is None else PropertyType(tag)


class ComponentPropertySchema(BasePropertySchema, ComponentPropertyTaggedFieldType):
    pass


class DefaultPropertySchema(BasePropertySchema):
    @property
    def type(self) -> PropertyType:
        return PropertyType.OBJECT


class StringPropertySchema(ComponentPropertySchema, tag=get_tag):
    pass


class IntegerPropertySchema(ComponentPropertySchema, tag=get_tag):
    pass


class NumberPropertySchema(ComponentPropertySchema, tag=get_tag):
    pass


class BooleanPropertySchema(ComponentPropertySchema, tag=get_tag):
    pass


class ObjectPropertySchema(ComponentPropertyTaggedFieldType, tag=get_tag):
    additional_properties: PropertySchema | None = msgspec.field(default=None, name="additionalProperties")
    properties: dict[str, Property] | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)
    required: list[str] = msgspec.field(default_factory=list)
    nullable: bool | None = msgspec.field(default=None)


class ArrayPropertySchema(ComponentPropertyTaggedFieldType, tag=get_tag):
    items: Property
    required: list[str] = msgspec.field(default_factory=list)
    description: str | None = msgspec.field(default=None)


class Component(Model):
    type: typing.Literal["object"]
    properties: dict[str, Property]
    required: list[str] = msgspec.field(default_factory=list)


class Components(Model):
    schemas: Schemas
    security_schemes: SecuritySchemes = msgspec.field(name="securitySchemes")


__all__ = ("Components",)
