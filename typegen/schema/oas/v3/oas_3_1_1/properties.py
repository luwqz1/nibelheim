import enum
import typing
from functools import cached_property

import msgspec

from typegen.model import Model, Union

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


class BasePropertySchema(Model):
    ref: str | None = msgspec.field(default=None, name="$ref")
    enum_values: list[typing.Any] | None = msgspec.field(default=None, name="enum")
    enum_names: list[str] | None = msgspec.field(default=None, name="x-enumNames")
    pattern: str | None = msgspec.field(default=None)
    properties: dict[str, Property] | None = msgspec.field(default=None)
    min_length: int | None = msgspec.field(default=None, name="minLength")
    max_length: int | None = msgspec.field(default=None, name="maxLength")
    minimum: int | float | None = msgspec.field(default=None)
    maximum: int | float | None = msgspec.field(default=None)
    exclusive_minimum: int | float | None = msgspec.field(default=None, name="exclusiveMinimum")
    exclusive_maximum: int | float | None = msgspec.field(default=None, name="exclusiveMaximum")
    default: typing.Any | None = msgspec.field(default=None)
    format: str | None = msgspec.field(default=None)
    examples: list[typing.Any] | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)
    nullable: bool | None = msgspec.field(default=None)

    @cached_property
    def desc(self) -> str | dict[str, typing.Any] | None:
        if self.description is None:
            return None

        try:
            return msgspec.json.decode(self.description)
        except msgspec.DecodeError:
            return self.description


class PropertySchema(BasePropertySchema, kw_only=True):
    type: str | None = msgspec.field(default=None)


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
    ref: str | None = msgspec.field(default=None, name="$ref")
    properties: dict[str, Property] | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)
    required: list[str] = msgspec.field(default_factory=list)
    nullable: bool | None = msgspec.field(default=None)


class ArrayPropertySchema(ComponentPropertyTaggedFieldType, tag=get_tag):
    items: Property
    ref: str | None = msgspec.field(default=None, name="$ref")
    required: list[str] = msgspec.field(default_factory=list)
    description: str | None = msgspec.field(default=None)


__all__ = ("BasePropertySchema", "Property", "PropertySchema", "PropertyType")
