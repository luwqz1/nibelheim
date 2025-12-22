import logging
import pathlib
import sys

from nibel.logger import configure
from typegen.generator import generate

if __name__ == "__main__":
    configure(level=logging.DEBUG)
    sys.exit(generate(workdir=pathlib.Path("nibel") / "types"))
