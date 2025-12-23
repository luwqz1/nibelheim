import typing

from typegen.model import Model


class Enums(Model):
    type From = str
    type To = str
    type Name = str
    type Description = str
    type EnumName = str
    type EnumValue = typing.Any

    renames: dict[From, To]
    class_descriptions: dict[Name, Description]
    enumerations_descriptions: dict[Name, dict[str, Description]]
    custom_enums: dict[Name, dict[EnumName, EnumValue]]


class GeneratorConfig(Model):
    enums: Enums


__all__ = ("GeneratorConfig",)
