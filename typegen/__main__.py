import pathlib
import sys

from typegen.generator import generate_remnawave

if __name__ == "__main__":
    sys.exit(
        generate_remnawave(
            workdir=pathlib.Path("src") / "nibel" / "remna",
            nicificated_schema_path=pathlib.Path(__file__).parent / "nicificated_schema.yaml",
        ),
    )
