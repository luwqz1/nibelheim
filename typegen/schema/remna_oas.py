import typing
from functools import cached_property

import msgspec
from packaging.version import Version, parse

from typegen.model import Model

type OASVersion = typing.Annotated[str, msgspec.Meta(pattern=r"^[0-9]+.[0-9]+.[0-9]$")]


class RemnaOAS(Model):
    oas: OASVersion = msgspec.field(name="openapi")

    @cached_property
    def version(self) -> Version:
        return parse(self.oas)


__all__ = ("OASVersion", "RemnaOAS")
