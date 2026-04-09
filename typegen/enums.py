from msgspex import BaseEnumMeta, StrEnum


class ALPN(StrEnum, metaclass=BaseEnumMeta):
    """Application-Layer Protocol Negotiation."""

    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"


class TemplateType(StrEnum, metaclass=BaseEnumMeta):
    """Type of template configuration for `Xray-Core`, `mihomo`, etc."""

    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class ClientType(StrEnum, metaclass=BaseEnumMeta):
    """Client type of subscription."""

    STASH = "stash"
    SINGBOX = "singbox"
    MIHOMO = "mihomo"
    JSON = "json"
    V2RAY_JSON = "v2ray-json"
    CLASH = "clash"


class ConditionsOperator(StrEnum, metaclass=BaseEnumMeta):
    """Operator to use for comparing the `headerName` with `value`."""

    EQUALS = "EQUALS"
    """Performs an exact, comparison between the header value and specified string.
    `string === value`."""

    NOT_EQUALS = "NOT_EQUALS"
    """Ensures the header value does not exactly match the specified string. `string
    !== value`."""

    CONTAINS = "CONTAINS"
    """Checks if the header value contains the specified string as a substring.
    `string.includes()`."""

    NOT_CONTAINS = "NOT_CONTAINS"
    """Verifies the header value does not contain the specified string as a substring.
    `!string.includes()`."""

    STARTS_WITH = "STARTS_WITH"
    """Validates that the header value begins with the specified string. `string.startsWith()`."""

    NOT_STARTS_WITH = "NOT_STARTS_WITH"
    """Validates that the header value does not begin with the specified string.
    `!string.startsWith()`."""

    ENDS_WITH = "ENDS_WITH"
    """Confirms the header value ends with the specified string. `string.endsWith()`."""

    NOT_ENDS_WITH = "NOT_ENDS_WITH"
    """Confirms the header value does not end with the specified string. `!string.endsWith()`."""

    REGEX = "REGEX"
    """Evaluates if the header value matches the specified regular expression
    pattern. `regex.test()`."""

    NOT_REGEX = "NOT_REGEX"
    """Evaluates if the header value does not match the specified regular expression
    pattern. `!regex.test()`."""


class Fingerprint(StrEnum, metaclass=BaseEnumMeta):
    """Simulate the TLS fingerprint using the `uTLS` library or it generate randomly."""

    CHROME = "chrome"
    """Simulate TLS fingerprint of the `Chrome` browser."""

    FIREFOX = "firefox"
    """Simulate TLS fingerprint of the `Firefox` browser."""

    SAFARI = "safari"
    """Simulate TLS fingerprint of the `Safari` browser."""

    IOS = "ios"
    """Simulate TLS fingerprint of the `iOS` browser."""

    ANDROID = "android"
    """Simulate TLS fingerprint of the `Android` browser."""

    EDGE = "edge"
    """Simulate TLS fingerprint of the `Edge` browser."""

    QQ = "qq"
    """Simulate TLS fingerprint of the `QQ` browser."""

    RANDOM = "random"
    """Rrandomly select one of the `up-to-date` browsers."""

    RANDOMIZED = "randomized"
    """Generate a completely random and unique fingerprint (100% compatible
    with `TLS 1.3` using `X25519`)."""


class Provider(StrEnum, metaclass=BaseEnumMeta):
    """OAuth2 authorization provider."""

    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"
    KEYCLOAK = "keycloak"
    GENERIC = "generic"


class ResponseRulesVersion(StrEnum, metaclass=BaseEnumMeta):
    """Response Rules Config Version."""

    V1 = "1"


class RulesOperator(StrEnum, metaclass=BaseEnumMeta):
    """Operator to use for combining conditions in the rule."""

    AND = "AND"
    OR = "OR"


class ResponseType(StrEnum, metaclass=BaseEnumMeta):
    """Type of the response. Determines the type of `response` to be returned when
    the rule is matched."""

    XRAY_JSON = "XRAY_JSON"
    """Return `subscription` in XRAY-JSON format. (Using `Xray Json` template)."""

    XRAY_BASE64 = "XRAY_BASE64"
    """Return `subscription` in BASE64 encoded string. Compatible with most
    client application with Xray core."""

    MIHOMO = "MIHOMO"
    """Return `subscription` in Mihomo format. (Using `Mihomo` template)."""

    STASH = "STASH"
    """Return `subscription` in Stash format. (Using `Stash` template)."""

    CLASH = "CLASH"
    """Return `subscription` in Clash format. (Using `Clash` template) Useful
    for client application that use Legacy Clash core."""

    SINGBOX = "SINGBOX"
    """Return `subscription` in Singbox format. (Using `Singbox` template)
    Format which is used by Singbox client application."""

    BROWSER = "BROWSER"
    """Return `subscription` as browser format. The same as on `/info` route."""

    BLOCK = "BLOCK"
    """`Drop` request and return `403` status code."""

    STATUS_CODE_404 = "STATUS_CODE_404"
    """`Drop` request and return `404` status code."""

    STATUS_CODE_451 = "STATUS_CODE_451"
    """`Drop` request and return `451` status code."""

    SOCKET_DROP = "SOCKET_DROP"
    """`Drop` the socket connection."""


class SecurityLayer(StrEnum, metaclass=BaseEnumMeta):
    """Transport layer encryption."""

    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"


class Status(StrEnum, metaclass=BaseEnumMeta):
    """User account status."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy(StrEnum, metaclass=BaseEnumMeta):
    """Available reset periods."""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class ConfigAction(StrEnum, metaclass=BaseEnumMeta):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class NodesAction(StrEnum, metaclass=BaseEnumMeta):
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    RESTART = "RESTART"
    RESET_TRAFFIC = "RESET_TRAFFIC"


class DropConnectionsTarget(StrEnum, metaclass=BaseEnumMeta):
    USERUUIDS = "userUuids"
    IPADDRESSES = "ipAddresses"
    ALLNODES = "allNodes"
    SPECIFICNODES = "specificNodes"


class EventScopeType(StrEnum, metaclass=BaseEnumMeta):
    CRM = "crm"
    SERVICE = "service"
    NODE = "node"
    USER = "user"
    USER_HWID_DEVICES = "user_hwid_devices"
    ERRORS = "errors"


class CRMEventType(StrEnum, metaclass=BaseEnumMeta):
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_7_DAYS = "crm.infra_billing_node_payment_in_7_days"
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_48HRS = "crm.infra_billing_node_payment_in_48hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_24HRS = "crm.infra_billing_node_payment_in_24hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_DUE_TODAY = "crm.infra_billing_node_payment_due_today"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_24HRS = "crm.infra_billing_node_payment_overdue_24hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_48HRS = "crm.infra_billing_node_payment_overdue_48hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_7_DAYS = "crm.infra_billing_node_payment_overdue_7_days"


class ServiceEventType(StrEnum, metaclass=BaseEnumMeta):
    SERVICE_PANEL_STARTED = "service.panel_started"
    SERVICE_LOGIN_ATTEMPT_FAILED = "service.login_attempt_failed"
    SERVICE_LOGIN_ATTEMPT_SUCCESS = "service.login_attempt_success"
    SERVICE_SUBPAGE_CONFIG_CHANGED = "service.subpage_config_changed"


class NodeEventType(StrEnum, metaclass=BaseEnumMeta):
    NODE_CREATED = "node.created"
    NODE_MODIFIED = "node.modified"
    NODE_DISABLED = "node.disabled"
    NODE_ENABLED = "node.enabled"
    NODE_DELETED = "node.deleted"
    NODE_CONNECTION_LOST = "node.connection_lost"
    NODE_CONNECTION_RESTORED = "node.connection_restored"
    NODE_TRAFFIC_NOTIFY = "node.traffic_notify"


class UserHwidDevicesEventType(StrEnum, metaclass=BaseEnumMeta):
    USER_HWID_DEVICES_ADDED = "user_hwid_devices.added"
    USER_HWID_DEVICES_DELETED = "user_hwid_devices.deleted"


class UserEventType(StrEnum, metaclass=BaseEnumMeta):
    USER_CREATED = "user.created"
    USER_MODIFIED = "user.modified"
    USER_DELETED = "user.deleted"
    USER_REVOKED = "user.revoked"
    USER_DISABLED = "user.disabled"
    USER_ENABLED = "user.enabled"
    USER_LIMITED = "user.limited"
    USER_EXPIRED = "user.expired"
    USER_TRAFFIC_RESET = "user.traffic_reset"
    USER_EXPIRES_IN_72_HOURS = "user.expires_in_72_hours"
    USER_EXPIRES_IN_48_HOURS = "user.expires_in_48_hours"
    USER_EXPIRES_IN_24_HOURS = "user.expires_in_24_hours"
    USER_EXPIRED_24_HOURS_AGO = "user.expired_24_hours_ago"
    USER_FIRST_CONNECTED = "user.first_connected"
    USER_BANDWIDTH_USAGE_THRESHOLD_REACHED = "user.bandwidth_usage_threshold_reached"
    USER_NOT_CONNECTED = "user.not_connected"


class ErrorsEventType(StrEnum, metaclass=BaseEnumMeta):
    ERRORS_BANDWIDTH_USAGE_THRESHOLD_REACHED_MAX_NOTIFICATIONS = "errors.bandwidth_usage_threshold_reached_max_notifications"
