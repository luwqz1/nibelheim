import logging
import pathlib

from nibel.logger import configure
from typegen.generator.generator import generate
from typegen.generator.objects import ObjectsGenerator

if __name__ == "__main__":
    configure(level=logging.DEBUG, service="nibelheim-typegen")
    generate(
        work_path=pathlib.Path("nibel/types"),
        objects_generator=ObjectsGenerator(),
    )
