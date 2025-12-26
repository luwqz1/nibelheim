import enum
import math
import sys
import typing

from nibel.logger import get_logger

NOT_SUPPORTED: typing.Final = "NOT_SUPPORTED"
ENUM_FRIENDS: typing.Final = (str, int, float)

logger = get_logger(__name__)


def _is_enum_friend(bases: tuple[type[typing.Any], ...], /) -> bool:
    return any(friend in bases for friend in ENUM_FRIENDS)


def _add_not_supported(classdict: dict[str, typing.Any], bases: tuple[type[typing.Any], ...], /) -> None:
    classdict["NOT_SUPPORTED"] = NOT_SUPPORTED if str in bases else math.inf if float in bases else sys.maxsize


class BaseEnumMeta(enum.EnumMeta, type):
    if typing.TYPE_CHECKING:

        class _BaseEnumMeta(enum.Enum):  # noqa
            NOT_SUPPORTED = enum.auto()

        NOT_SUPPORTED: typing.Literal[_BaseEnumMeta.NOT_SUPPORTED]

    else:

        @staticmethod
        def _member_missing(cls, value):
            logger.warning(
                "Unsupported value {!r} for enum of type {!r}. Probably nibelheim needs to be updated to support the latest version of Remnawave API.",
                value,
                cls,
            )
            return cls._member_map_["NOT_SUPPORTED"]

        def __new__(
            metacls,
            cls,
            bases,
            classdict,
            *,
            boundary=None,
            _simple=False,
            **kwds,
        ):
            if _is_enum_friend(bases):
                _add_not_supported(classdict, bases)
            else:
                for base in bases:
                    if _is_enum_friend(base.__bases__):
                        _add_not_supported(classdict, base.__bases__)
                        break

            classdict["_missing_"] = classmethod(BaseEnumMeta._member_missing)
            new_type = super().__new__(metacls, cls, bases, classdict, boundary=boundary, _simple=_simple, **kwds)
            return new_type


__all__ = ("BaseEnumMeta",)
