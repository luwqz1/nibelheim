import keyword
import types
import typing
from functools import cache
from reprlib import recursive_repr

import msgspec
from fntypes.library.monad.option import Nothing

MODEL_CONFIG: typing.Final = {
    "dict": True,
    "rename": {kw + "_": kw for kw in keyword.kwlist},
}
UNSET: typing.Final = typing.cast("typing.Any", msgspec.UNSET)
NOTHING: typing.Final = Nothing()


def struct_asdict(
    struct: msgspec.Struct,
    /,
    *,
    exclude_unset: bool = True,
    unset_as_nothing: bool = False,
) -> dict[str, typing.Any]:
    return {
        k: v if not unset_as_nothing else NOTHING if v is msgspec.UNSET else v
        for k, v in msgspec.structs.asdict(struct).items()
        if not (exclude_unset and isinstance(v, msgspec.UnsetType | types.NoneType | Nothing))
    }


class Model(msgspec.Struct, **MODEL_CONFIG):
    def __getattribute__(self, name: str, /) -> typing.Any:
        cls = type(self)
        val = object.__getattribute__(self, name)

        if name not in cls.__struct_fields__:
            return val

        if (
            (field_info := cls.get_fields().get(name)) is not None
            and isinstance(field_info.type, msgspec.inspect.CustomType)
            and issubclass(field_info.type.cls, Model)
        ):
            return Nothing() if val is UNSET else val

        if val is UNSET:
            raise AttributeError(f"{cls.__name__!r} object has no attribute {name!r}")

        return val

    def __post_init__(self) -> None:
        for name, field in struct_asdict(self, exclude_unset=False).items():
            if isinstance(field, Nothing | types.NoneType):
                setattr(self, name, UNSET)

    @recursive_repr()
    def __repr__(self) -> str:
        return "{}({})".format(
            type(self).__name__,
            ", ".join(f"{name}={value!r}" for name, value in struct_asdict(self, exclude_unset=False, unset_as_nothing=True).items()),
        )

    @classmethod
    @cache
    def get_fields(cls) -> types.MappingProxyType[str, msgspec.inspect.Field]:
        return types.MappingProxyType(
            mapping={f.name: f for f in getattr(msgspec.inspect.type_info(cls), "fields", ())},
        )

    @classmethod
    def from_data[**P, T](cls, *args: typing.Any, **kwargs: typing.Any) -> typing.Self: ...

    @classmethod
    def from_dict(cls, obj: dict[str, typing.Any], /) -> typing.Self: ...

    @classmethod
    def from_raw(cls, raw: str | bytes | msgspec.Raw, /) -> typing.Self: ...

    def to_raw(self) -> str: ...

    def to_dict(
        self,
        *,
        exclude_fields: set[str] | None = None,
    ) -> dict[str, typing.Any]:
        return self._to_dict("model_as_dict", exclude_fields or set(), False)

    def to_full_dict(
        self,
        *,
        exclude_fields: set[str] | None = None,
    ) -> dict[str, typing.Any]:
        return self._to_dict("model_as_full_dict", exclude_fields or set(), True)

    def _to_dict(self, dct_name: str, exclude_fields: set[str], full: bool) -> dict[str, typing.Any]:
        if dct_name not in self.__dict__:
            self.__dict__[dct_name] = struct_asdict(self) if not full else {}

        if not exclude_fields:
            return self.__dict__[dct_name]

        return {k: v for k, v in self.__dict__[dct_name].items() if k not in exclude_fields}


__all__ = ("Model",)
