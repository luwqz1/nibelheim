import keyword
import pathlib
import re
import subprocess
import sys
import typing

import jinja2
import msgspec
import niquests
from packaging.version import parse
from typegen.generator.code.property_type import CODEGEN_PROPERTY_TYPE_MAP, IMPORTS

from nibel.logger import get_logger
from typegen.cfg.config import Config
from typegen.config import read_config
from typegen.generator.oas import OAS as OAS_GENERATOR
from typegen.model import decode_hook
from typegen.schema.oas import OAS as OAS_SCHEMA
from typegen.schema.remna_oas import RemnaOAS

if typing.TYPE_CHECKING:
    from typegen.generator.abc import Context

LOG: typing.Final = get_logger(__name__)
MAX_LENGTH_LINE_CHUNK: typing.Final = 60
DEFAULTS_IN_DESCRIPTION_PATTERN: typing.Final = re.compile(r"\s*Defaults to\b[^.;:\n\r]*[.;:]?")


def to_pascal_case(s: str, /) -> str:
    if "_" in s:
        return "".join(to_pascal_case(c) for c in s.split("_"))
    return s[0].upper() + s[1:]


def to_snake_case(s: str, /) -> str:
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in s).lstrip("_")


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


def run_command(command: str, /) -> bool:
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="UTF-8",
    )
    return result.returncode == 0


def run_ruff_formatter(workdir: pathlib.Path, /) -> None:
    LOG.info("Run ruff-format...")
    if not run_command(f"ruff format {workdir}"):
        LOG.error("ruff formatter failed.")
    else:
        LOG.info("ruff formatter successfully formatted files!")

    LOG.info("Run ruff-isort...")
    if not run_command(f"ruff check {workdir} --select I --select F401 --fix"):
        LOG.error("ruff-isort failed.")
    else:
        LOG.info("ruff-isort successfully sorted imports!")

    LOG.info("Run ruff-sortall...")
    if not run_command(f"ruff check {workdir} --select RUF022 --fix"):
        LOG.error("ruff-sortall failed.")
    else:
        LOG.info("ruff-sortall successfully sorted dunder alls!")


def generate(
    workdir: pathlib.Path,
    config_path: pathlib.Path,
    templates_loader: jinja2.FileSystemLoader | None = None,
) -> int:
    LOG.debug("Reading config from `{!s}`...", config_path)
    config = read_config(config_path).as_model(Config)
    LOG.debug("Config read successfully!")

    try:
        LOG.debug("Downloading Remnawave API schema from `{!s}`...", config.remnawave.oas_url)
        raw_response = niquests.get(url=config.remnawave.oas_url).content  # type: ignore
        LOG.debug("Remnawave API schema downloaded successfully!")
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

    if remna_api.version == parse(config.remnawave.version):
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
            snake_case=to_snake_case,
            makesafe_name=makesafe_name,
            codegen_property_type_map=CODEGEN_PROPERTY_TYPE_MAP,
            imports="\n".join(IMPORTS),
            chunks_str=chunks_str,
            refactor_field_description=refactor_field_description_for_class_docstring,
        ),
    )
    context: Context = dict(config=config)

    print("\n", file=sys.stderr)

    for generator in OAS_GENERATOR[remna_oas.version.major][remna_oas.version]:
        generator.generate(remna_api, context, environment, workdir)  # type: ignore

    # run_ruff_formatter(workdir)
    return 0


__all__ = ("generate",)
