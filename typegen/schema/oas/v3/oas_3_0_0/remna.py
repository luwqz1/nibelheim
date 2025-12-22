from functools import cached_property

from packaging.version import Version, parse

from typegen.model import Model
from typegen.schema.oas.v3.oas_3_0_0.components import Components
from typegen.schema.oas.v3.oas_3_0_0.paths import Paths
from typegen.schema.oas.v3.oas_3_0_0.tags import Tags


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
