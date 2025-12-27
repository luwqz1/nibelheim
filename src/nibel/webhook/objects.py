import enum
import typing

from nibel.model import From, Model, Option, datetime, field
from nibel.webhook.enums import NodeEvent, NodeInfraBillingEvent, ServiceEvent, UpdateType, UserEvent

type Data = typing.Any


class RawUpdate(typing.TypedDict):
    event: str
    data: Data
    timestamp: datetime


class Event[E: enum.Enum](Model, kw_only=True):
    event: E
    """The event that occurred."""

    timestamp: datetime
    """The timestamp of the webhook payload."""


# NOTE: Inherit from nibel.types.objects.UserDTO
class User(Event[UserEvent]):
    pass


# NOTE: Inherit from nibel.types.objects.NodeDTO
class Node(Event[NodeEvent]):
    pass


# NOTE: Inherit from nibel.types.objects.BillingNodeDTO
class NodeInfraBilling(Event[NodeInfraBillingEvent]):
    pass


class Service(Event[ServiceEvent]):
    # NOTE: implement login_attempt field
    pass


class Update(Model):
    """This object represents an incoming update of the event from the webhook server."""

    type: UpdateType
    """The type of update that occurred."""

    timestamp: datetime
    """The timestamp of the webhook payload."""

    user: Option[User] = field(default=..., converter=From[User | None])
    """Optional. New incoming user event."""

    node: Option[Node] = field(default=..., converter=From[Node | None])
    """Optional. New incoming node event."""

    node_infra_billing: Option[NodeInfraBilling] = field(default=..., converter=From[NodeInfraBilling | None])
    """Optional. New incoming node infra billing event."""

    service: Option[Service] = field(default=..., converter=From[Service | None])
    """Optional. New incoming service event."""


__all__ = ("Node", "NodeInfraBilling", "Service", "Update", "User")
