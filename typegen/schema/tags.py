import msgspec

type Tags = list[Tag]


class Tag(msgspec.Struct):
    name: str
    description: str | None = msgspec.field(default=None)


__all__ = ("Tags",)
