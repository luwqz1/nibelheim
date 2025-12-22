import msgspec

from typegen.model import Model

type Tags = list[Tag]


class Tag(Model):
    name: str
    description: str | None = msgspec.field(default=None)


__all__ = ("Tags",)
