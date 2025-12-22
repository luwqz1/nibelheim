import typing

from packaging.version import parse

from typegen.schema.oas.v3.oas_3_1_1 import components, paths, properties, remna, security, tags

OAS_3_1_1: typing.Final = parse("3.1.1")

__all__ = ("OAS_3_1_1", "components", "paths", "properties", "remna", "security", "tags")
