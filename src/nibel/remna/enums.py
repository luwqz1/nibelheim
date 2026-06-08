import msgspex


class Status(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """User account status."""

    ACTIVE = "ACTIVE"
    """User account is active."""

    DISABLED = "DISABLED"
    """User account is disabled."""

    LIMITED = "LIMITED"
    """User account is limited."""

    EXPIRED = "EXPIRED"
    """User account has expired."""


class TrafficLimitStrategy(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Available reset periods."""

    NO_RESET = "NO_RESET"
    """Traffic limit is never reset."""

    DAY = "DAY"
    """Traffic limit resets daily."""

    WEEK = "WEEK"
    """Traffic limit resets weekly."""

    MONTH = "MONTH"
    """Traffic limit resets monthly."""

    MONTH_ROLLING = "MONTH_ROLLING"
    """Traffic limit resets monthly by creation date."""


class SecurityLayer(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Transport layer encryption."""

    DEFAULT = "DEFAULT"
    """Use the default transport layer encryption behavior."""

    TLS = "TLS"
    """Use TLS transport layer encryption."""

    NONE = "NONE"
    """Disable transport layer encryption."""


class TemplateType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Type of template configuration for `Xray-Core`, `mihomo`, etc."""

    XRAY_JSON = "XRAY_JSON"
    """Xray template in JSON format."""

    XRAY_BASE64 = "XRAY_BASE64"
    """Xray template as Base64-encoded content."""

    MIHOMO = "MIHOMO"
    """Template for Mihomo clients."""

    STASH = "STASH"
    """Template for Stash clients."""

    CLASH = "CLASH"
    """Template for Clash clients."""

    SINGBOX = "SINGBOX"
    """Template for Singbox clients."""


class NodesAction(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Action to apply to nodes."""

    ENABLE = "ENABLE"
    """Enable selected nodes."""

    DISABLE = "DISABLE"
    """Disable selected nodes."""

    RESTART = "RESTART"
    """Restart selected nodes."""

    RESET_TRAFFIC = "RESET_TRAFFIC"
    """Reset traffic counters for selected nodes."""


class ALPN(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Application-Layer Protocol Negotiation."""

    H3 = "h3"
    """HTTP/3 only."""

    H2 = "h2"
    """HTTP/2 only."""

    HTTP_1_1 = "http/1.1"
    """HTTP/1.1 only."""

    H_COMBINED = "h2,http/1.1"
    """Combined HTTP/2 and HTTP/1.1 ALPN."""

    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    """Combined HTTP/3, HTTP/2, and HTTP/1.1 ALPN."""

    H3_H2_COMBINED = "h3,h2"
    """Combined HTTP/3 and HTTP/2 ALPN."""


class Fingerprint(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
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
    """Generate a completely random and unique fingerprint (100% compatible with `TLS 1.3` using `X25519`)."""


class ResponseRulesVersion(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Response Rules Config Version."""

    V1 = "1"
    """Response rules configuration version 1."""


class RulesOperator(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Operator to use for combining conditions in the rule."""

    AND = "AND"
    """All conditions in the rule must match."""

    OR = "OR"
    """Any condition in the rule may match."""


class ConditionsOperator(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Operator to use for comparing the `headerName` with `value`."""

    EQUALS = "EQUALS"
    """Performs an exact comparison between the header value and specified string. `string === value`."""

    NOT_EQUALS = "NOT_EQUALS"
    """Ensures the header value does not exactly match the specified string. `string !== value`."""

    CONTAINS = "CONTAINS"
    """Checks if the header value contains the specified string as a substring. `string.includes()`."""

    NOT_CONTAINS = "NOT_CONTAINS"
    """Verifies the header value does not contain the specified string as a substring. `!string.includes()`."""

    STARTS_WITH = "STARTS_WITH"
    """Validates that the header value begins with the specified string. `string.startsWith()`."""

    NOT_STARTS_WITH = "NOT_STARTS_WITH"
    """Validates that the header value does not begin with the specified string. `!string.startsWith()`."""

    ENDS_WITH = "ENDS_WITH"
    """Confirms the header value ends with the specified string. `string.endsWith()`."""

    NOT_ENDS_WITH = "NOT_ENDS_WITH"
    """Confirms the header value does not end with the specified string. `!string.endsWith()`."""

    REGEX = "REGEX"
    """Evaluates if the header value matches the specified regular expression pattern. `regex.test()`."""

    NOT_REGEX = "NOT_REGEX"
    """Evaluates if the header value does not match the specified regular expression pattern. `!regex.test()`."""


class ResponseType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Type of the response. Determines the type of `response` to be returned when the rule is matched."""

    XRAY_JSON = "XRAY_JSON"
    """Return `subscription` in XRAY-JSON format. (Using `Xray Json` template)."""

    XRAY_BASE64 = "XRAY_BASE64"
    """Return `subscription` in BASE64 encoded string. Compatible with most client application with Xray core."""

    MIHOMO = "MIHOMO"
    """Return `subscription` in Mihomo format. (Using `Mihomo` template)."""

    STASH = "STASH"
    """Return `subscription` in Stash format. (Using `Stash` template)."""

    CLASH = "CLASH"
    """Return `subscription` in Clash format. (Using `Clash` template) Useful for client application that use Legacy Clash core."""

    SINGBOX = "SINGBOX"
    """Return `subscription` in Singbox format. (Using `Singbox` template) Format which is used by Singbox client application."""

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


class DropConnectionsTarget(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Target scope for dropping connections."""

    USER_UUIDS = "userUuids"
    """Drop connections by user UUIDs."""

    IP_ADDRESSES = "ipAddresses"
    """Drop connections by IP addresses."""

    ALL_NODES = "allNodes"
    """Drop connections on all nodes."""

    SPECIFIC_NODES = "specificNodes"
    """Drop connections on specific nodes."""


class ProxyConfigsProtocol(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    VLESS = "vless"
    TROJAN = "trojan"
    SHADOWSOCKS = "shadowsocks"
    HYSTERIA = "hysteria"


class ProxyConfigsProtocolOptionsFlow(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    NOTHING = ""
    XTLS_RPRX_VISION = "xtls-rprx-vision"
    XTLS_RPRX_VISION_UDP443 = "xtls-rprx-vision-udp443"


class ProxyConfigsTransport(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    TLS = "tcp"
    XHTTP = "xhttp"
    WS = "ws"
    HTTPUPGRADE = "httpupgrade"
    GRPC = "grpc"
    KCP = "kcp"
    HYSTERIA = "hysteria"


class ProxyConfigsTransportOptionsHeader(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    HTTP = "http"
    NONE = "none"


class ProxyConfigsTransportOptionsMode(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    AUTO = "auto"
    PACKET_UP = "packet-up"
    STREAM_UP = "stream-up"
    STREAM_ONE = "stream-one"


class ProxyConfigsSecurity(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    TLS = "tls"
    REALITY = "reality"
    NONE = "none"


class Provider(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """OAuth2 authorization provider."""

    GITHUB = "github"
    """GitHub OAuth2 provider."""

    POCKETID = "pocketid"
    """Pocket ID OAuth2 provider."""

    YANDEX = "yandex"
    """Yandex OAuth2 provider."""

    KEYCLOAK = "keycloak"
    """Keycloak OAuth2 provider."""

    GENERIC = "generic"
    """Generic OAuth2 provider."""

    TELEGRAM = "telegram"
    """Telegram OAuth2 provider."""


class PluginExecutorCommand(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    BLOCK_IPS = "blockIps"
    RECREATE_TABLES = "recreateTables"


class EventScopeType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Scope of the emitted event."""

    CRM = "crm"
    """CRM event scope."""

    SERVICE = "service"
    """Service event scope."""

    NODE = "node"
    """Node event scope."""

    USER = "user"
    """User event scope."""

    USER_HWID_DEVICES = "user_hwid_devices"
    """User HWID devices event scope."""

    TORRENT_BLOCKER = "torrent_blocker"
    """Torrent blocker event scope."""

    ERRORS = "errors"
    """Errors event scope."""


class CRMEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """CRM event type."""

    CRM_INFRA_BILLING_NODE_PAYMENT_IN_7_DAYS = "crm.infra_billing_node_payment_in_7_days"
    """Node payment is due in 7 days."""

    CRM_INFRA_BILLING_NODE_PAYMENT_IN_48HRS = "crm.infra_billing_node_payment_in_48hrs"
    """Node payment is due in 48 hours."""

    CRM_INFRA_BILLING_NODE_PAYMENT_IN_24HRS = "crm.infra_billing_node_payment_in_24hrs"
    """Node payment is due in 24 hours."""

    CRM_INFRA_BILLING_NODE_PAYMENT_DUE_TODAY = "crm.infra_billing_node_payment_due_today"
    """Node payment is due today."""

    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_24HRS = "crm.infra_billing_node_payment_overdue_24hrs"
    """Node payment is overdue by 24 hours."""

    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_48HRS = "crm.infra_billing_node_payment_overdue_48hrs"
    """Node payment is overdue by 48 hours."""

    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_7_DAYS = "crm.infra_billing_node_payment_overdue_7_days"
    """Node payment is overdue by 7 days."""


class ErrorsEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Error event type."""

    ERRORS_BANDWIDTH_USAGE_THRESHOLD_REACHED_MAX_NOTIFICATIONS = "errors.bandwidth_usage_threshold_reached_max_notifications"
    """Maximum bandwidth usage threshold notifications reached."""


class NodeEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Node event type."""

    NODE_CREATED = "node.created"
    """Node was created."""

    NODE_MODIFIED = "node.modified"
    """Node was modified."""

    NODE_DISABLED = "node.disabled"
    """Node was disabled."""

    NODE_ENABLED = "node.enabled"
    """Node was enabled."""

    NODE_DELETED = "node.deleted"
    """Node was deleted."""

    NODE_CONNECTION_LOST = "node.connection_lost"
    """Node connection was lost."""

    NODE_CONNECTION_RESTORED = "node.connection_restored"
    """Node connection was restored."""

    NODE_TRAFFIC_NOTIFY = "node.traffic_notify"
    """Node traffic notification was emitted."""


class ServiceEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Service event type."""

    SERVICE_PANEL_STARTED = "service.panel_started"
    """Panel service started."""

    SERVICE_LOGIN_ATTEMPT_FAILED = "service.login_attempt_failed"
    """Login attempt failed."""

    SERVICE_LOGIN_ATTEMPT_SUCCESS = "service.login_attempt_success"
    """Login attempt succeeded."""

    SERVICE_SUBPAGE_CONFIG_CHANGED = "service.subpage_config_changed"
    """Subpage configuration changed."""


class ConfigAction(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Action applied to the configuration."""

    CREATED = "CREATED"
    """Configuration was created."""

    UPDATED = "UPDATED"
    """Configuration was updated."""

    DELETED = "DELETED"
    """Configuration was deleted."""


class TorrentBlockerEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Torrent blocker event type."""

    TORRENT_BLOCKER_REPORT = "torrent_blocker.report"


class UserEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """User event type."""

    USER_CREATED = "user.created"
    """User was created."""

    USER_MODIFIED = "user.modified"
    """User was modified."""

    USER_DELETED = "user.deleted"
    """User was deleted."""

    USER_REVOKED = "user.revoked"
    """User was revoked."""

    USER_DISABLED = "user.disabled"
    """User was disabled."""

    USER_ENABLED = "user.enabled"
    """User was enabled."""

    USER_LIMITED = "user.limited"
    """User was limited."""

    USER_EXPIRED = "user.expired"
    """User expired."""

    USER_TRAFFIC_RESET = "user.traffic_reset"
    """User traffic was reset."""

    USER_EXPIRES_IN_72_HOURS = "user.expires_in_72_hours"
    """User expires in 72 hours."""

    USER_EXPIRES_IN_48_HOURS = "user.expires_in_48_hours"
    """User expires in 48 hours."""

    USER_EXPIRES_IN_24_HOURS = "user.expires_in_24_hours"
    """User expires in 24 hours."""

    USER_EXPIRED_24_HOURS_AGO = "user.expired_24_hours_ago"
    """User expired 24 hours ago."""

    USER_FIRST_CONNECTED = "user.first_connected"
    """User connected for the first time."""

    USER_BANDWIDTH_USAGE_THRESHOLD_REACHED = "user.bandwidth_usage_threshold_reached"
    """User reached the bandwidth usage threshold."""

    USER_NOT_CONNECTED = "user.not_connected"
    """User has not connected."""


class UserHwidDevicesEventType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """User HWID devices event type."""

    USER_HWID_DEVICES_ADDED = "user_hwid_devices.added"
    """User HWID device was added."""

    USER_HWID_DEVICES_DELETED = "user_hwid_devices.deleted"
    """User HWID device was deleted."""


class ClientType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Client type of subscription."""

    STASH = "stash"
    """Subscription for Stash client."""

    SINGBOX = "singbox"
    """Subscription for Singbox client."""

    MIHOMO = "mihomo"
    """Subscription for Mihomo client."""

    JSON = "json"
    """Subscription in JSON format."""

    V2RAY_JSON = "v2ray-json"
    """Subscription in V2Ray JSON format."""

    CLASH = "clash"
    """Subscription for Clash client."""


__all__ = (
    "ALPN",
    "CRMEventType",
    "ClientType",
    "ConditionsOperator",
    "ConfigAction",
    "DropConnectionsTarget",
    "ErrorsEventType",
    "EventScopeType",
    "Fingerprint",
    "NodeEventType",
    "NodesAction",
    "PluginExecutorCommand",
    "Provider",
    "ProxyConfigsProtocol",
    "ProxyConfigsProtocolOptionsFlow",
    "ProxyConfigsSecurity",
    "ProxyConfigsTransport",
    "ProxyConfigsTransportOptionsHeader",
    "ProxyConfigsTransportOptionsMode",
    "ResponseRulesVersion",
    "ResponseType",
    "RulesOperator",
    "SecurityLayer",
    "ServiceEventType",
    "Status",
    "TemplateType",
    "TorrentBlockerEventType",
    "TrafficLimitStrategy",
    "UserEventType",
    "UserHwidDevicesEventType",
)
