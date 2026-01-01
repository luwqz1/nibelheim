import datetime as dt
import typing
from annotationlib import type_repr
from contextlib import contextmanager

import fntypes.library
import msgspec

from nibel.model.msgspec_utils.caster import SupportsCast
from nibel.model.msgspec_utils.custom_types.datetime import datetime, timedelta
from nibel.model.msgspec_utils.custom_types.enum import BaseEnumMeta
from nibel.model.msgspec_utils.custom_types.literal import _Literal  # type: ignore
from nibel.model.msgspec_utils.custom_types.option import Option
from nibel.model.msgspec_utils.type_check import is_common_type, type_check

type Context = dict[str, typing.Any]
type DecHook[T] = typing.Callable[typing.Concatenate[type[T], typing.Any, ...], typing.Any]


def option_dec_hook(
    tp: type[Option[typing.Any]],
    obj: typing.Any,
    /,
) -> fntypes.library.Option[typing.Any] | msgspec.UnsetType:
    if obj is msgspec.UNSET:
        return obj

    if obj is None or isinstance(obj, fntypes.library.Nothing):
        return fntypes.library.Nothing()

    (value_type,) = typing.get_args(tp) or (typing.Any,)
    orig_value_type = typing.get_origin(value_type) or value_type
    orig_obj = obj

    if not isinstance(orig_obj, dict | list) and is_common_type(orig_value_type):
        if orig_value_type is fntypes.library.Variative:
            obj = value_type(orig_obj)  # type: ignore
            orig_value_type = typing.get_args(value_type)

        if not type_check(orig_obj, orig_value_type):
            raise msgspec.ValidationError(
                f"Expected `{type_repr(orig_value_type)}` or `builtins.None`, got `{type_repr(orig_obj)}`.",
            )

        return fntypes.library.Some(obj)  # type: ignore

    return fntypes.library.Some(decoder.convert(orig_obj, type=value_type))  # type: ignore


def variative_dec_hook(
    tp: type[fntypes.library.Variative],  # type: ignore
    obj: typing.Any,
    /,
) -> typing.Any:
    union_types = typing.get_args(tp)

    if isinstance(obj, dict):
        reverse = False
        models_fields_count: dict[type[msgspec.Struct], int] = {
            m: sum(1 for k in obj if k in m.__struct_fields__)  # type: ignore
            for m in union_types
            if issubclass(typing.get_origin(m) or m, msgspec.Struct)
        }
        union_types = tuple(t for t in union_types if t not in models_fields_count)

        if len(set(models_fields_count.values())) != len(models_fields_count.values()):
            models_fields_count = {m: len(m.__struct_fields__) for m in models_fields_count}
            reverse = True

        union_types = (
            *sorted(
                models_fields_count,
                key=lambda k: models_fields_count[k],
                reverse=reverse,
            ),
            *union_types,
        )

    if not isinstance(obj, dict | list) and any(is_common_type(t) and type_check(obj, t) for t in union_types):
        return tp(obj)  # type: ignore

    for t in union_types:
        match convert(obj, t):
            case fntypes.library.Ok(value):
                return tp(value)  # type: ignore
            case fntypes.library.Error(_):
                continue

    raise msgspec.ValidationError(
        "Object of type `{}` doesn't belong to `{}[{}]`.".format(
            type_repr(obj),  # type: ignore
            type_repr(fntypes.library.Variative),
            ", ".join(type_repr(typing.get_origin(x) or x) for x in union_types),
        )
    )


def datetime_dec_hook(tp: type[datetime], obj: typing.Any, /) -> datetime:
    if isinstance(obj, datetime):
        return obj

    if isinstance(obj, dt.datetime):
        assert issubclass(tp, SupportsCast)
        return tp.cast(obj)

    if isinstance(obj, int | float):
        return tp.fromtimestamp(timestamp=obj)

    raise TypeError(
        "Cannot validate object of type `{}` into `datetime.datetime`".format(
            type_repr(obj),
        ),
    )


def timedelta_dec_hook(tp: type[timedelta], obj: typing.Any, /) -> timedelta:
    if isinstance(obj, timedelta):
        return obj

    if isinstance(obj, dt.timedelta):
        assert issubclass(tp, SupportsCast)
        return tp.cast(obj)

    if isinstance(obj, int | float):
        return tp(seconds=obj)

    raise TypeError(
        "Cannot validate object of type `{}` into `datetime.timedelta`".format(
            type_repr(obj),
        ),
    )


def convert[T](
    obj: typing.Any,
    t: type[T],
    /,
) -> fntypes.library.Result[T, str]:
    try:
        return fntypes.library.Ok(decoder.convert(obj, type=t, strict=True))
    except msgspec.ValidationError:
        return fntypes.library.Error(
            "Expected object of type `{}`, got `{}`.".format(
                type_repr(t),
                type_repr(obj),
            )
        )


def literal_dec_hook(literal: type[_Literal], obj: typing.Any, /) -> typing.Any:
    if obj in literal.__args__:
        return obj

    raise msgspec.ValidationError(
        "Invalid literal value {!r} of either {}.".format(
            obj,
            literal.__args__[0] if len(literal.__args__) == 1 else (", ".join(f"`{x}`" for x in literal.__args__[:-1])) + f" or `{literal.__args__[-1]}`",
        )
    )


class Decoder:
    dec_hooks: dict[typing.Any, DecHook[typing.Any]]
    abstract_dec_hooks: dict[typing.Any, DecHook[typing.Any]]

    def __init__(self) -> None:
        self.dec_hooks = {
            Option: option_dec_hook,
            fntypes.library.Variative: variative_dec_hook,
            datetime: datetime_dec_hook,
            timedelta: timedelta_dec_hook,
            fntypes.library.Some: option_dec_hook,
            fntypes.library.Nothing: option_dec_hook,
        }
        self.abstract_dec_hooks = {
            BaseEnumMeta: lambda enum_type, member: enum_type(member),
            _Literal: literal_dec_hook,
        }

    def __repr__(self) -> str:
        return "<{}: dec_hooks={!r}, abstract_dec_hooks={!r}>".format(
            type(self).__name__,
            self.dec_hooks,
            self.abstract_dec_hooks,
        )

    @typing.overload
    def __call__[T](
        self,
        type: type[T],
    ) -> typing.ContextManager[msgspec.json.Decoder[T]]: ...

    @typing.overload
    def __call__(
        self,
        type: typing.Any,
    ) -> typing.ContextManager[msgspec.json.Decoder[typing.Any]]: ...

    @typing.overload
    def __call__[T](
        self,
        type: type[T],
        *,
        strict: bool = True,
    ) -> typing.ContextManager[msgspec.json.Decoder[T]]: ...

    @typing.overload
    def __call__(
        self,
        type: typing.Any,
        *,
        strict: bool = True,
    ) -> typing.ContextManager[msgspec.json.Decoder[typing.Any]]: ...

    @contextmanager
    def __call__(
        self,
        type: typing.Any = object,
        *,
        strict: bool = True,
    ) -> typing.Generator[msgspec.json.Decoder[typing.Any], typing.Any, None]:
        yield msgspec.json.Decoder(
            type=typing.Any if type is object else type,
            strict=strict,
            dec_hook=self.dec_hook,
        )

    def add_dec_hook[T](self, t: type[T], /) -> typing.Callable[[DecHook[T]], DecHook[T]]:
        def decorator(func: DecHook[T], /) -> DecHook[T]:
            return self.dec_hooks.setdefault(typing.get_origin(t) or t, func)

        return decorator

    def add_abstract_dec_hook[T](self, abstract_type: type[T], /) -> typing.Callable[[DecHook[T]], DecHook[T]]:
        def decorator(func: DecHook[T], /) -> DecHook[T]:
            return self.abstract_dec_hooks.setdefault(typing.get_origin(abstract_type) or abstract_type, func)

        return decorator

    def get_abstract_dec_hook(self, subtype: type[typing.Any], /) -> DecHook[typing.Any] | None:
        for abstract, dec_hook in self.abstract_dec_hooks.items():
            if issubclass(subtype, abstract) or issubclass(type(subtype), abstract):
                return dec_hook

        return None

    def dec_hook(self, tp: typing.Any, obj: typing.Any, /) -> DecHook[typing.Any]:
        origin_type = typing.get_origin(tp) or tp

        if (dec_hook_func := self.dec_hooks.get(origin_type)) is None and (dec_hook_func := self.get_abstract_dec_hook(origin_type)) is None:
            raise NotImplementedError(
                f"Not implemented decode hook for type `{type_repr(origin_type)}`. You can implement decode hook for this type.",
            )

        return dec_hook_func(tp, obj)

    def convert[T](
        self,
        obj: object,
        *,
        type: type[T] = dict,
        strict: bool = True,
        from_attributes: bool = False,
        builtin_types: typing.Iterable[type[typing.Any]] | None = None,
        str_keys: bool = False,
    ) -> T:
        return msgspec.convert(
            obj,
            type,
            strict=strict,
            from_attributes=from_attributes,
            dec_hook=self.dec_hook,
            builtin_types=builtin_types,
            str_keys=str_keys,
        )

    @typing.overload
    def decode(
        self,
        buf: str | bytes,
    ) -> typing.Any: ...

    @typing.overload
    def decode[T](
        self,
        buf: str | bytes,
        *,
        type: type[T],
    ) -> T: ...

    @typing.overload
    def decode(
        self,
        buf: str | bytes,
        *,
        type: typing.Any,
    ) -> typing.Any: ...

    @typing.overload
    def decode[T](
        self,
        buf: str | bytes,
        *,
        type: type[T],
        strict: bool = True,
    ) -> T: ...

    @typing.overload
    def decode(
        self,
        buf: str | bytes,
        *,
        type: typing.Any,
        strict: bool = True,
    ) -> typing.Any: ...

    def decode(
        self,
        buf: str | bytes,
        *,
        type: typing.Any = object,
        strict: bool = True,
    ) -> typing.Any:
        return msgspec.json.decode(
            buf,
            type=typing.Any if type is object else type,
            strict=strict,
            dec_hook=self.dec_hook,
        )


decoder: typing.Final = Decoder()


__all__ = ("Decoder", "convert", "decoder")
