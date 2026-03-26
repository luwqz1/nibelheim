import pathlib
import sys

from typegen.generator import generate

if __name__ == "__main__":
    sys.exit(
        generate(
            workdir=pathlib.Path("src") / "nibel" / "types",
            config_path=pathlib.Path(__file__).parent / "config.toml",
        ),
    )
