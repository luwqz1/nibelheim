import pathlib
import typing

import msgspec
import msgspex


class Model(msgspex.Model, omit_defaults=True):
    pass


class Remnawave(Model):
    schema_url: str
    schema_document_type: typing.Literal["json", "yaml"]
    errors_schema_url: str


class EnumSchema(Model):
    name: str
    members: list[str]
    values: list[str | int | float]
    description: str | None = None
    member_descriptions: dict[str, str] = msgspex.field(default_factory=dict[str, str])


class Schema(Model):
    type EnumName = str

    enums: dict[EnumName, EnumSchema] = msgspex.field(default_factory=dict[EnumName, EnumSchema])


class NicificatedSchema(Model):
    remnawave: Remnawave
    schema: Schema


def read_schema(path: pathlib.Path | None = None, /) -> NicificatedSchema:
    path = path or pathlib.Path(__file__).with_suffix(".yaml")
    raw = msgspec.yaml.decode(path.read_bytes())

    if isinstance(raw, dict) and isinstance(raw.get("remnawave"), dict) and "schema" in raw["remnawave"]:  # type: ignore
        raw["schema"] = raw["remnawave"].pop("schema")  # type: ignore

    if isinstance(raw, dict) and isinstance(raw.get("schema"), dict) and isinstance(raw["schema"].get("enums"), list):  # type: ignore
        enums_dict: dict[str, typing.Any] = {}

        for item in raw["schema"]["enums"]:  # type: ignore
            if isinstance(item, dict):
                enums_dict.update(item)  # type: ignore

        raw["schema"]["enums"] = enums_dict

    return msgspec.convert(raw, type=NicificatedSchema)


def write_schema(schema: NicificatedSchema, path: pathlib.Path | None = None, /) -> None:
    path = path or pathlib.Path(__file__).with_suffix(".yaml")

    enums: list[dict[str, typing.Any]] = []
    for enum_key, enum_schema in schema.schema.enums.items():
        enum_data: dict[str, typing.Any] = {
            "name": enum_schema.name,
            "members": enum_schema.members,
            "values": enum_schema.values,
        }

        if enum_schema.description is not None:
            enum_data["description"] = enum_schema.description

        if enum_schema.member_descriptions:
            enum_data["member_descriptions"] = enum_schema.member_descriptions

        enums.append({enum_key: enum_data})

    document = {
        "remnawave": {
            "schema_url": schema.remnawave.schema_url,
            "schema_document_type": schema.remnawave.schema_document_type,
            "errors_schema_url": schema.remnawave.errors_schema_url,
            "schema": {
                "enums": enums,
            },
        },
    }

    path.write_bytes(msgspec.yaml.encode(document))


__all__ = ("read_schema", "write_schema")
