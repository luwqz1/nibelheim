import typing

import fntypes.library
import msgspec

_NOTHING: typing.Final = fntypes.library.Nothing()
_COMMON_TYPES: typing.Final = frozenset((str, int, float, bool, None, fntypes.library.Variative))


def is_common_type[T](t: T, /) -> typing.TypeGuard[type[T]]:
    if not isinstance(t, type):
        return False
    return t in _COMMON_TYPES or issubclass(t, msgspec.Struct) or hasattr(t, "__dataclass_fields__")  # type: ignore


def type_check(obj: typing.Any, t: typing.Any) -> bool:
    return isinstance(obj, t) if isinstance(t, type) and issubclass(t, msgspec.Struct) else type(obj) in t if isinstance(t, tuple) else type(obj) is t


__all__ = ("is_common_type", "type_check")
