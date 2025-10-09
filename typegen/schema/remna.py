import typing

import msgspec

from typegen.model import Model
from typegen.schema.components import Components
from typegen.schema.paths import Paths
from typegen.schema.tags import Tags


class Info(Model):
    title: str
    description: str
    version: str
    contact: typing.Any
    license: typing.Any


class RemnaAPI(Model):
    openapi: str
    info: Info
    tags: Tags
    paths: Paths
    servers: list[typing.Any]
    components: Components
    description: str | None = msgspec.field(default=None)


__all__ = ("RemnaAPI",)
