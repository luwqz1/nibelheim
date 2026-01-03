import keyword
import os
import pathlib
import re
import typing

import jinja2
import msgspec
import niquests
from packaging.version import parse

from nibel.logger import get_logger
from src.__remna__ import __api_spec_url__, __version__
from typegen.cfg.config import Config
from typegen.config import read_config
from typegen.generator.oas import OAS as OAS_GENERATOR
from typegen.model import decode_hook
from typegen.schema.oas import OAS as OAS_SCHEMA
from typegen.schema.remna_oas import RemnaOAS

if typing.TYPE_CHECKING:
    from typegen.generator.abc import Context

REMNA_API_VERSION: typing.Final = parse(__version__)
LOG: typing.Final = get_logger(__name__)
MAX_LENGTH_LINE_CHUNK: typing.Final = 60
DEFAULTS_IN_DESCRIPTION_PATTERN: typing.Final = re.compile(r"\s*Defaults to\b[^.;:\n\r]*[.;:]?")


def to_pascal_case(s: str, /) -> str:
    if "_" in s:
        return "".join(to_pascal_case(c) for c in s.split("_"))
    return s[0].upper() + s[1:]


def makesafe_name(s: str, /) -> str:
    return f"{s}_" if keyword.iskeyword(s) else s


def chunks_str(s: str, sep: str = "\n    ") -> str:
    chunked_string, line_length = "", 0

    for word in s.split():
        chunked_string += word + " "
        line_length += len(word)

        if line_length >= MAX_LENGTH_LINE_CHUNK:
            chunked_string = chunked_string.strip() + sep
            line_length = 0

    return chunked_string.rstrip()


def refactor_field_description_for_class_docstring(description: str, /) -> str:
    description = description.removeprefix("Optional. ")
    description = DEFAULTS_IN_DESCRIPTION_PATTERN.sub("", description)
    if not description.endswith("."):
        description += "."
    return description.replace("**", "`").strip()


def run_ruff_formatter(workdir: pathlib.Path, /) -> None:
    LOG.debug("Run ruff-format...")
    if os.system(f"ruff format {workdir}") != 0:
        LOG.error("ruff formatter failed.")
    else:
        LOG.info("ruff formatter successfully formatted files!")

    LOG.debug("Run ruff-isort...")
    if os.system(f"ruff check {workdir} --select I --select F401 --fix") != 0:
        LOG.error("ruff-isort failed.")
    else:
        LOG.info("ruff-isort successfully sorted imports!")

    LOG.debug("Run ruff-sortall...")
    if os.system(f"ruff check {workdir} --select RUF022 --fix") != 0:
        LOG.error("ruff-sortall failed.")
    else:
        LOG.info("ruff-sortall successfully sorted dunder alls!")


def generate(
    workdir: pathlib.Path,
    config_path: pathlib.Path,
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
            "Remnawave Open API Specification version `{}` is not supported. Only supported versions: {}.",
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
    environment.globals.update(
        dict(  # type: ignore
            pascal_case=to_pascal_case,
            makesafe_name=makesafe_name,
            chunks_str=chunks_str,
            refactor_field_description=refactor_field_description_for_class_docstring,
        ),
    )
    context: Context = dict(config=read_config(config_path).as_model(Config))

    for generator in OAS_GENERATOR[remna_oas.version.major][remna_oas.version]:
        generator.generate(remna_api, context, environment, workdir)  # type: ignore

    run_ruff_formatter(workdir)
    return 0


__all__ = ("generate",)
