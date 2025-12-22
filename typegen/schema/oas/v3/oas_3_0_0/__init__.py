import typing

from packaging.version import parse

from typegen.schema.oas.v3.oas_3_0_0 import components, paths, properties, remna, security, tags

OAS_3_0_0: typing.Final = parse("3.0.0")

__all__ = ("OAS_3_0_0", "components", "paths", "properties", "remna", "security", "tags")
