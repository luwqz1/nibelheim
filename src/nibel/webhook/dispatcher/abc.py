import abc


class ABCDispatcher(abc.ABC):
    @abc.abstractmethod
    async def feed(self) -> None:
        pass


__all__ = ("ABCDispatcher",)
