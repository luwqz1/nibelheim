import typing

from typegen.model import Model
from typegen.schema.components import Components
from typegen.schema.paths import Paths
from typegen.schema.tags import Tags


class Info(Model):
    title: str
    description: str
    version: str


class RemnaAPI(Model):
    openapi: str
    info: Info
    tags: Tags
    paths: Paths
    servers: list[typing.Any]
    components: Components


__all__ = ("RemnaAPI",)
