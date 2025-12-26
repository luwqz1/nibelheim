import keyword
import types
import typing
from functools import cache
from reprlib import recursive_repr

import fntypes.library
import msgspec
from fntypes.library.monad.option import Nothing
from msgspec import field as _field

from nibel.model.msgspec_utils.decoder import decoder
from nibel.model.msgspec_utils.encoder import encoder

NOTHING: typing.Final = fntypes.library.Nothing()
UNSET: typing.Final = typing.cast("typing.Any", msgspec.UNSET)
MODEL_CONFIG: typing.Final = {
    "dict": True,
    "rename": {kw + "_": kw for kw in keyword.kwlist},
}


def is_none(obj: typing.Any, /) -> typing.TypeIs[Nothing | None]:
    return isinstance(obj, Nothing | types.NoneType)


def model_asdict(
    struct: msgspec.Struct,
    /,
    *,
    exclude_unset: bool = True,
    unset_as_nothing: bool = False,
) -> dict[str, typing.Any]:
    return {
        k: v if not unset_as_nothing else NOTHING if v is msgspec.UNSET else v
        for k, v in msgspec.structs.asdict(struct).items()
        if not (exclude_unset and isinstance(v, msgspec.UnsetType | types.NoneType | fntypes.library.Nothing))
    }


def field(**kwargs: typing.Any) -> typing.Any:
    if kwargs.get("default") is Ellipsis:
        kwargs["default"] = UNSET

    kwargs.pop("converter", None)
    return _field(**kwargs)


@typing.dataclass_transform(field_specifiers=(field,))
class Model(msgspec.Struct, **MODEL_CONFIG):
    if not typing.TYPE_CHECKING:

        def __init_subclass__(cls, *args: typing.Any, **kwargs: typing.Any) -> None:
            from telegrinder.tools.member_descriptor_proxy import MemberDescriptorProxy

            result = super().__init_subclass__(*args, **kwargs)

            for field_name in getattr(cls, "__slots__", ()):
                setattr(cls, field_name, MemberDescriptorProxy(getattr(cls, field_name)))

            return result

        def __getattribute__(self, name: str, /) -> typing.Any:
            class_ = type(self)
            val = object.__getattribute__(self, name)

            if name not in class_.__struct_fields__:
                return val

            if (
                (field_info := class_.get_fields().get(name)) is not None
                and isinstance(field_info.type, msgspec.inspect.CustomType)
                and issubclass(field_info.type.cls, Option)
            ):
                return Nothing() if val is UNSET else val

            if val is UNSET:
                raise AttributeError(f"{class_.__name__!r} object has no attribute {name!r}")

            return val

    def __post_init__(self) -> None:
        for field, value in model_asdict(self, exclude_unset=False).items():
            if is_none(value):
                setattr(self, field, UNSET)

    @recursive_repr()
    def __repr__(self) -> str:
        return "{}({})".format(
            type(self).__name__,
            ", ".join(f"{f}={val!r}" for f, val in model_asdict(self, exclude_unset=False, unset_as_nothing=True).items()),
        )

    @classmethod
    @cache
    def get_fields(cls) -> types.MappingProxyType[str, msgspec.inspect.Field]:
        return types.MappingProxyType(
            mapping={f.name: f for f in msgspec.inspect.type_info(cls).fields},  # type: ignore
        )

    @classmethod
    def from_data[**P, T](cls: typing.Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
        return decoder.convert(msgspec.structs.asdict(cls(*args, **kwargs)), type=cls)  # type: ignore

    @classmethod
    def from_dict(cls, obj: dict[str, typing.Any], /) -> typing.Self:
        return decoder.convert(obj, type=cls)

    @classmethod
    def from_raw(cls, raw: str | bytes, /) -> typing.Self:
        return decoder.decode(raw, type=cls)

    def _to_dict(
        self,
        dct_name: str,
        exclude_fields: set[str],
        full: bool,
    ) -> dict[str, typing.Any]:
        if dct_name not in self.__dict__:
            self.__dict__[dct_name] = (
                model_asdict(self) if not full else encoder.to_builtins(self.to_dict(exclude_fields=exclude_fields), order="deterministic")
            )

        if not exclude_fields:
            return self.__dict__[dct_name]

        return {key: value for key, value in self.__dict__[dct_name].items() if key not in exclude_fields}

    def to_raw(self) -> str:
        return encoder.encode(self)

    def to_dict(
        self,
        *,
        exclude_fields: set[str] | None = None,
    ) -> dict[str, typing.Any]:
        return self._to_dict("model_as_dict", exclude_fields or set(), full=False)

    def to_full_dict(
        self,
        *,
        exclude_fields: set[str] | None = None,
    ) -> dict[str, typing.Any]:
        return self._to_dict("model_as_full_dict", exclude_fields or set(), full=True)


__all__ = ("MODEL_CONFIG", "UNSET", "Model", "field", "is_none", "model_asdict")
