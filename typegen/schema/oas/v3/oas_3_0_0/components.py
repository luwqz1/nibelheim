import msgspec

from typegen.model import Model
from typegen.schema.oas.v3.oas_3_0_0.properties import Property
from typegen.schema.oas.v3.oas_3_0_0.security import SecuritySchemes

type Schemas = dict[str, Component]


class Component(Model):
    type: str
    properties: dict[str, Property]
    required: list[str] = msgspec.field(default_factory=list)


class Components(Model):
    schemas: Schemas
    security_schemes: SecuritySchemes = msgspec.field(name="securitySchemes")


__all__ = ("Components",)
