import pathlib
import typing

import jinja2
import msgspec
import niquests
from packaging.version import parse

from nibel.logger import get_logger
from src.__remna__ import __api_spec_url__, __version__
from typegen.generator.oas import OAS as OAS_GENERATOR
from typegen.model import decode_hook
from typegen.schema.oas import OAS as OAS_SCHEMA
from typegen.schema.remna_oas import RemnaOAS

if typing.TYPE_CHECKING:
    from typegen.generator.abc import Context

REMNA_API_VERSION: typing.Final = parse(__version__)
LOG: typing.Final = get_logger(__name__)


def to_pascal_case(s: str, /) -> str:
    if "_" in s:
        return "".join(to_pascal_case(c) for c in s.split("_"))
    return s[0].upper() + s[1:]


def generate(
    workdir: pathlib.Path,
    templates_loader: jinja2.FileSystemLoader | None = None,
) -> int:
    try:
        raw_response = niquests.get(url=__api_spec_url__).content  # type: ignore
    except Exception as e:
        LOG.error("Failed to download Remnawave API schema with error: '{!s}'", e)
        return 1

    if not raw_response:
        LOG.error("Failed to download Remnawave API schema.")
        return 1

    remna_oas = msgspec.json.decode(raw_response, type=RemnaOAS)
    if remna_oas.version.major not in OAS_SCHEMA or remna_oas.version not in OAS_SCHEMA[remna_oas.version.major]:
        is_supported_major_version = remna_oas.version.major in OAS_SCHEMA
        LOG.error(
            "Remnawave Open API Schema version `{}` is not supported. Only supported versions: {}.",
            f"{remna_oas.version.major}.x.x" if not is_supported_major_version else remna_oas.version,
            ", ".join(
                map(
                    lambda x: f"`{x}.x.x`" if not is_supported_major_version else f"`{x}`",
                    OAS_SCHEMA[remna_oas.version.major] if not is_supported_major_version else [remna_oas.version],
                ),
            ),
        )
        return 1

    schema = OAS_SCHEMA[remna_oas.version.major][remna_oas.version]
    remna_api = msgspec.json.decode(raw_response, type=schema.remna.RemnaAPI, dec_hook=decode_hook)

    if remna_api.version == REMNA_API_VERSION:
        LOG.info("Remnawave API version `{}` | OAS `{}` is up to date, skipping generation.", remna_api.version, remna_oas.version)
        return 0

    LOG.warning("New Remnawave API version `{}` | OAS `{}` detected, running generator...", remna_api.version, remna_oas.version)

    environment = jinja2.Environment(
        loader=templates_loader or jinja2.FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.globals["pascal_case"] = to_pascal_case  # type: ignore
    context: Context = dict()

    for generator in OAS_GENERATOR[remna_oas.version.major][remna_oas.version]:
        generator.generate(remna_api, context, environment, workdir)  # type: ignore

    return 0


__all__ = ("generate",)
