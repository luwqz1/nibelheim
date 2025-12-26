import abc


class ABCReceiver(abc.ABC):
    @abc.abstractmethod
    async def receive(self) -> None:
        pass


__all__ = ("ABCReceiver",)
