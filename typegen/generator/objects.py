import dataclasses
import os
import pathlib
import typing

import jinja2
from typegen.schema.components import ObjectPropertySchema, Property
from typegen.schema.remna import RemnaAPI

from typegen.generator.generator import ABCGenerator, Context

TEMPLATE_NAME: typing.Final = "objects.j2"
IMPORTS_LINES: typing.Final = (
    "import typing\n\n",
    "from msgspec import Meta\n\n",
    "from nibel.model.base import Model, From, field\n\n",
)


def pascal_to_snake(name: str) -> str:
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in name).lstrip("_")


@dataclasses.dataclass(frozen=True, slots=True)
class Ref:
    name: str
    path: str


class ObjectsGenerator(ABCGenerator):
    def _process_lines(self, lines: list[str]) -> list[str]: ...

    def generate(
        self,
        work_path: pathlib.Path,
        remna_api: RemnaAPI,
        jinja_env: jinja2.Environment,
        context: Context,
    ) -> None:
        refs: dict[str, Ref] = {}
        objects_path = work_path / "objects"
        lines: list[str] = list(IMPORTS_LINES)

        for component_name, component in remna_api.components.schemas.items():
            name = component_name.removesuffix("Dto")
            refs.setdefault(
                f"#/components/schemas/{component_name}",
                Ref(name, path=str(objects_path / f"{pascal_to_snake(component_name)}").replace(os.sep, ".")),
            )

            properties = [component.properties.copy()]
            processed_props: list[dict[str, Property]] = []

            while properties:
                props = properties.pop()

                for prop_name, prop in props.copy().items():
                    if isinstance(prop, ObjectPropertySchema) and prop.properties:
                        properties.append(prop.properties)
                        props.pop(prop_name, None)

                processed_props.append(props)

            for props in processed_props:
                lines.extend(
                    jinja_env.get_template(TEMPLATE_NAME).render(
                        component_name=name + ("DTO" if props == processed_props[-1] else ""),
                        properties=props,
                    ),
                )

        context["components_refs"] = refs
        self._process_lines(lines)


__all__ = ("ObjectsGenerator",)
