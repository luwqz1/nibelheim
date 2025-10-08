import msgspec


class Security(msgspec.Struct):
    scheme: str
    name: str
    type: str | None = msgspec.field(default=None)
    bearer_format: str | None = msgspec.field(default=None, name="bearerFormat")
    description: str | None = msgspec.field(default=None)


class SecuritySchemes(msgspec.Struct):
    authorization: Security = msgspec.field(name="Authorization")
    prometheus: Security = msgspec.field(name="Prometheus")


__all__ = ("Security", "SecuritySchemes")
