import types
import typing

import msgspec

def model_asdict(
    model: Model,
    /,
    *,
    exclude_unset: bool = ...,
    unset_as_nothing: bool = ...,
) -> dict[str, typing.Any]: ...

@typing.overload
def field() -> typing.Any: ...
@typing.overload
def field(*, name: str | None = ...) -> typing.Any: ...
@typing.overload
def field(
    *,
    default: typing.Any | None = ...,
    name: str | None = ...,
) -> typing.Any: ...
@typing.overload
def field(
    *,
    default_factory: typing.Callable[[], typing.Any] | None = ...,
    name: str | None = ...,
) -> typing.Any: ...
@typing.overload
def field(
    *,
    default: typing.Any | None = ...,
    converter: typing.Callable[[typing.Any], typing.Any] | None = ...,
    name: str | None = ...,
) -> typing.Any: ...
@typing.overload
def field(
    *,
    default_factory: typing.Callable[[], typing.Any] | None = ...,
    converter: typing.Callable[[typing.Any], typing.Any] | None = ...,
    name: str | None = ...,
) -> typing.Any: ...
@typing.overload
def field(
    *,
    default: typing.Any | None = ...,
    default_factory: typing.Callable[[], typing.Any] | None = ...,
    converter: typing.Callable[[typing.Any], typing.Any] | None = ...,
    name: str | None = ...,
) -> typing.Any: ...

class From[T]:
    def __new__(cls, _: T) -> T: ...

class Model(msgspec.Struct):
    @classmethod
    def get_fields(cls) -> types.MappingProxyType[str, typing.Any]: ...
    @classmethod
    def from_data[**P, T](
        cls: typing.Callable[P, T],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> T: ...  # type: ignore
    @classmethod
    def from_dict(cls, obj: dict[str, typing.Any], /) -> typing.Self: ...
    @classmethod
    def from_raw(cls, raw: str | bytes | msgspec.Raw, /) -> typing.Self: ...
    def to_raw(self) -> str: ...
    def to_dict(
        self,
        *,
        exclude_fields: set[str] | None = ...,
    ) -> dict[str, typing.Any]: ...
    def to_full_dict(
        self,
        *,
        exclude_fields: set[str] | None = ...,
    ) -> dict[str, typing.Any]: ...
