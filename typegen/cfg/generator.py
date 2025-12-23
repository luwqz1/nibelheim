from typegen.model import Model


class Enums(Model):
    type From = str
    type To = str
    type Name = str
    type Description = str

    renames: dict[From, To]
    class_descriptions: dict[Name, Description]
    enumerations_descriptions: dict[Name, dict[str, Description]]


class GeneratorConfig(Model):
    enums: Enums


__all__ = ("GeneratorConfig",)
