import msgspec

from typegen.schema.components import Components
from typegen.schema.paths import Paths
from typegen.schema.tags import Tags


class Info(msgspec.Struct):
    title: str
    description: str
    version: str


class RemnaAPI(msgspec.Struct):
    openapi: str
    info: Info
    tags: Tags
    paths: Paths
    components: Components


__all__ = ("RemnaAPI",)
