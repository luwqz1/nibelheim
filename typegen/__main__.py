import logging
import pathlib
import sys

from jinja2 import FileSystemLoader

from nibel.logger import configure
from typegen.generator import generate

if __name__ == "__main__":
    configure(level=logging.DEBUG)
    sys.exit(
        generate(
            workdir=pathlib.Path("src") / "nibel" / "types",
            config_path=pathlib.Path(__file__).parent / "config.toml",
            templates_loader=FileSystemLoader(pathlib.Path(__file__).parent / "generator" / "templates"),
        ),
    )
