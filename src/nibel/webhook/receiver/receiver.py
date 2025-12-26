from nibel.webhook.receiver.abc import ABCReceiver


# NOTE: Implement the receiver
class Receiver(ABCReceiver):
    async def receive(self) -> None:
        pass


__all__ = ("Receiver",)
