import typing

import msgspec


class BasePropertySchema(msgspec.Struct):
    ref: str | None = msgspec.field(default=None, name="$ref")
    enum_values: list[typing.Any] | None = msgspec.field(default=None, name="enum")
    enum_names: list[str] | None = msgspec.field(default=None, name="x-enumNames")
    pattern: str | None = msgspec.field(default=None)
    min_length: int | None = msgspec.field(default=None, name="minLength")
    max_length: int | None = msgspec.field(default=None, name="maxLength")
    minimum: int | float | None = msgspec.field(default=None)
    maximum: int | float | None = msgspec.field(default=None)
    exclusive_minimum: bool | None = msgspec.field(default=None, name="exclusiveMinimum")
    exclusive_maximum: bool | None = msgspec.field(default=None, name="exclusiveMaximum")
    default: typing.Any | None = msgspec.field(default=None)
    format: str | None = msgspec.field(default=None)
    example: typing.Any | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)
    nullable: bool | None = msgspec.field(default=None)


class PropertySchema(BasePropertySchema, kw_only=True):
    type: str | None = msgspec.field(default=None)


__all__ = ("BasePropertySchema", "PropertySchema")
