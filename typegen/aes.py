"""Remnawave API Errors Specification."""

import typing
from functools import cached_property

import msgspec
from packaging.version import Version, parse

from typegen.model import Model

type RemnawaveVersion = typing.Annotated[str, msgspec.Meta(pattern=r"^[0-9]+.[0-9]+.[0-9]$")]
type ErrorName = str
type Errors = dict[ErrorName, Error]


class Error(Model):
    message: str
    error_code: str = msgspec.field(name="errorCode")


class RemnawaveAES(Model):
    remnawave: RemnawaveVersion
    errors: Errors

    @cached_property
    def remna_version(self) -> Version:
        return parse(self.remnawave)


__all__ = ("RemnawaveAES",)
