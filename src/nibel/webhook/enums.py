import enum

from nibel.model.msgspec_utils.custom_types.enum_meta import BaseEnumMeta


class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value


class UpdateType(StrEnum):
    """Type of update."""

    USER = "user"
    NODE = "node"
    NODE_INFRA_BILLING = "node_infra_billing"
    SERVICE = "service"


class UserEvent(StrEnum, metaclass=BaseEnumMeta):
    """Type of user event."""

    CREATED = "created"
    """The user was created."""

    MODIFIED = "modified"
    """The user was modified."""

    DELETED = "deleted"
    """The user was deleted."""

    REVOKED = "revoked"
    """The user was revoked."""

    DISABLED = "disabled"
    """The user was disabled."""

    ENABLED = "enabled"
    """The user was enabled."""

    LIMITED = "limited"
    """The user was limited."""

    EXPIRED = "expired"
    """The user was expired."""

    TRAFFIC_RESET = "traffic_reset"
    """The user's traffic was reset."""

    EXPIRES_IN_72_HOURS = "expires_in_72_hours"
    """The user's subscription will expire in 72 hours."""

    EXPIRES_IN_48_HOURS = "expires_in_48_hours"
    """The user's subscription will expire in 48 hours."""

    EXPIRES_IN_24_HOURS = "expires_in_24_hours"
    """The user's subscription will expire in 24 hours."""

    EXPIRED_24_HOURS_AGO = "expired_24_hours_ago"
    """The user's subscription expired 24 hours ago."""

    FIRST_CONNECT = "first_connect"
    """The user connected to the node for the first time."""

    BANDWIDTH_USAGE_THRESHOLD_REACHED = "bandwidth_usage_threshold_reached"
    """The user's bandwidth usage threshold was reached."""


class NodeEvent(StrEnum, metaclass=BaseEnumMeta):
    """Type of node event."""

    CREATED = "created"
    """Node was created."""

    MODIFIED = "modified"
    """Node was modified."""

    DELETED = "deleted"
    """Node was deleted."""

    DISABLED = "disabled"
    """Node was disabled."""

    ENABLED = "enabled"
    """Node was enabled."""

    CONNECTION_LOST = "connection_lost"
    """Node's connection was lost."""

    CONNECTION_RESTORED = "connection_restored"
    """Node's connection was restored."""

    TRAFFIC_NOTIFY = "traffic_notify"
    """Node reached the traffic notify limit."""


class NodeInfraBillingEvent(StrEnum, metaclass=BaseEnumMeta):
    """Type of node infra billing event."""

    INFRA_BILLING_NODE_PAYMENT_IN_7_DAYS = "infra_billing_node_payment_in_7_days"
    """Payment reminder 7 days in advance."""

    INFRA_BILLING_NODE_PAYMENT_IN_48_HOURS = "infra_billing_node_payment_in_48hrs"
    """Payment reminder 48 hours in advance."""

    INFRA_BILLING_NODE_PAYMENT_IN_24_HOURS = "infra_billing_node_payment_in_24hrs"
    """Payment reminder 24 hours in advance."""

    INFRA_BILLING_NODE_PAYMENT_DUE_TODAY = "infra_billing_node_payment_due_today"
    """Payment reminder on the due date."""

    INFRA_BILLING_NODE_PAYMENT_OVERDUE_24_HOURS = "infra_billing_node_payment_overdue_24hrs"
    """Overdue payment notification after 24 hours."""

    INFRA_BILLING_NODE_PAYMENT_OVERDUE_48_HOURS = "infra_billing_node_payment_overdue_48hrs"
    """Overdue payment notification after 48 hours."""

    INFRA_BILLING_NODE_PAYMENT_OVERDUE_7_DAYS = "infra_billing_node_payment_overdue_7_days"
    """Overdue payment notification after 7 days."""


class ServiceEvent(StrEnum, metaclass=BaseEnumMeta):
    """Type of service event."""

    PANEL_STARTED = "panel_started"
    """The service started."""

    LOGIN_ATTEMPT_FAILED = "login_attempt_failed"
    """The login attempt failed."""

    LOGIN_ATTEMPT_SUCCESS = "login_attempt_success"
    """The login attempt was successful."""


__all__ = ("NodeEvent", "NodeInfraBillingEvent", "ServiceEvent", "UpdateType", "UserEvent")
