import typing

import msgspec

from typegen.model import Model


class BasePropertySchema(Model):
    ref: str | None = msgspec.field(default=None, name="$ref")
    enum_values: list[typing.Any] | None = msgspec.field(default=None, name="enum")
    enum_names: list[str] | None = msgspec.field(default=None, name="x-enumNames")
    pattern: str | None = msgspec.field(default=None)
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


class PropertySchema(BasePropertySchema, kw_only=True):
    type: str | None = msgspec.field(default=None)


__all__ = ("BasePropertySchema", "PropertySchema")
