from nibel.webhook.dispatcher.abc import ABCDispatcher


# NOTE: Implement the dispatcher
class Dispatcher(ABCDispatcher):
    async def feed(self) -> None:
        pass


__all__ = ("Dispatcher",)
