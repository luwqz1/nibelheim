import typing

import msgspec

if typing.TYPE_CHECKING:
    from typegen.schema.properties import BasePropertySchema


def decode_hook(
    type: typing.Any,
    obj: typing.Any,
) -> "BasePropertySchema":
    if not issubclass(type, _Union) or not isinstance(obj, dict):
        raise NotImplementedError

    if "type" not in obj:
        return msgspec.convert(obj, type=type.__args__[0])  # type: ignore

    tagged_union = typing.Union[*type.__args__[:-1]]  # type: ignore
    return msgspec.convert(obj, type=tagged_union, dec_hook=decode_hook)


class _UnionMeta(type):
    def __instancecheck__(cls, instance: typing.Any) -> bool:
        return isinstance(instance, getattr(cls, "__args__"))


class _Union(metaclass=_UnionMeta):
    __args__: tuple[typing.Any, ...]

    def __class_getitem__(cls, items: typing.Any) -> typing.Any:
        return type("_Union", (cls,), {"__args__": (items,) if not isinstance(items, tuple) else items})


class Model(msgspec.Struct):
    pass


if typing.TYPE_CHECKING:
    Union = typing.Union
else:
    Union = _Union


__all__ = ("Model", "decode_hook")
