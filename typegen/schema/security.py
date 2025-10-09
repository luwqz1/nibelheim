import msgspec

from typegen.model import Model


class Security(Model):
    scheme: str
    name: str
    type: str | None = msgspec.field(default=None)
    bearer_format: str | None = msgspec.field(default=None, name="bearerFormat")
    description: str | None = msgspec.field(default=None)


class SecuritySchemes(Model):
    authorization: Security = msgspec.field(name="Authorization")
    prometheus: Security = msgspec.field(name="Prometheus")


__all__ = ("Security", "SecuritySchemes")
