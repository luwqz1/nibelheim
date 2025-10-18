import dataclasses
import os
import os.path
import pathlib

import jinja2

from typegen.generator.generator import ABCGenerator, Context
from typegen.schema.remna import RemnaAPI


def pascal_to_snake(name: str) -> str:
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in name).lstrip("_")


@dataclasses.dataclass(frozen=True, slots=True)
class Ref:
    name: str
    path: str


class ObjectsGenerator(ABCGenerator):
    def generate(
        self,
        work_path: pathlib.Path,
        remna_api: RemnaAPI,
        jinja_env: jinja2.Environment,
        context: Context,
    ) -> None:
        refs: dict[str, Ref] = {}
        objects_path = work_path / "objects"

        for component_name, component in remna_api.components.schemas.items():
            name = component_name.removesuffix("Dto") + "DTO"
            refs.setdefault(
                f"#/components/schemas/{component_name}",
                Ref(name, path=os.path.splitext(objects_path / f"{pascal_to_snake(component_name)}.py")[0].replace(os.sep, ".")),
            )


__all__ = ("ObjectsGenerator",)
