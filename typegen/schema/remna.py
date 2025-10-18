import typing
from functools import cached_property

import msgspec
from packaging.version import Version, parse

from typegen.model import Model
from typegen.schema.components import Components
from typegen.schema.paths import Paths
from typegen.schema.tags import Tags

type OASVersion = typing.Annotated[str, msgspec.Meta(pattern=r"^[0-9]+.[0-9]+.[0-9]$")]


class OAS(Model):
    oas_version: OASVersion = msgspec.field(name="openapi")

    @cached_property
    def version(self) -> Version:
        return parse(self.oas_version)


class Info(Model):
    title: str
    description: str
    version: str


class RemnaAPI(Model):
    info: Info
    tags: Tags
    paths: Paths
    components: Components

    @cached_property
    def version(self) -> Version:
        return parse(self.info.version)


__all__ = ("RemnaAPI",)
