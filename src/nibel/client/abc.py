import abc
import typing


class ABCClient(abc.ABC):
    async def __aenter__(self) -> typing.Self:
        return self

    async def __aexit__(
        self,
        exc_type: typing.Any,
        exc_value: typing.Any,
        traceback: typing.Any,
    ) -> None:
        await self.close()

    @abc.abstractmethod
    async def close(self) -> None:
        pass

    @property
    @abc.abstractmethod
    def timeout(self) -> float: ...

    @abc.abstractmethod
    async def request_text(
        self,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> str: ...

    @abc.abstractmethod
    async def request_json(self, *args: typing.Any, **kwargs: typing.Any) -> dict[str, typing.Any]:
        pass

    @abc.abstractmethod
    async def request_content(self, *args: typing.Any, **kwargs: typing.Any) -> bytes:
        pass

    @abc.abstractmethod
    async def request_bytes(self, *args: typing.Any, **kwargs: typing.Any) -> bytes:
        pass


__all__ = ("ABCClient",)
