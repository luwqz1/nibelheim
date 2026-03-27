import msgspex


class Status(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Traffic limit reset strategy"""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class SecurityLayer(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"


class BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class BulkNodesActionsRequestDtoAction(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    RESTART = "RESTART"
    RESET_TRAFFIC = "RESET_TRAFFIC"


class HostRequestDtoAlpn(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H2_HTTP_1_1 = "h2,http/1.1"
    H3_H2_HTTP_1_1 = "h3,h2,http/1.1"
    H3_H2 = "h3,h2"


class HostRequestDtoFingerprint(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"


class CreateUserRequestDtoStatus(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Optional. User account status. Defaults to ACTIVE."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy2(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """Available reset periods"""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class DebugSrrMatcherRequestDtoResponseRulesVersion(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """{"title":"Response Rules Config Version","markdownDescription":"Version of the **response rules** config. Currently supported version is **1**."}"""

    VALUE_1 = "1"


class DebugSrrMatcherRequestDtoResponseRulesRulesOperator(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """{"markdownDescription":"Operator to use for combining conditions in the rule."}"""

    AND = "AND"
    OR = "OR"


class DebugSrrMatcherRequestDtoResponseRulesRulesConditionsOperator(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """{"errorMessage":"Invalid operator. Please select a valid operator.","markdownDescription":"Operator to use for comparing the `headerName` with `value`.","markdownEnumDescriptions":["Performs an exact, comparison between the header value and specified string. `string === value`","Ensures the header value does not exactly match the specified string. `string !== value`","Checks if the header value contains the specified string as a substring. `string.includes()`","Verifies the header value does not contain the specified string as a substring. `!string.includes()`","Validates that the header value begins with the specified string. `string.startsWith()`","Validates that the header value does not begin with the specified string. `!string.startsWith()`","Confirms the header value ends with the specified string. `string.endsWith()`","Confirms the header value does not end with the specified string. `!string.endsWith()`","Evaluates if the header value matches the specified regular expression pattern. `regex.test()`","Evaluates if the header value does not match the specified regular expression pattern. `!regex.test()`"]}"""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    NOT_STARTS_WITH = "NOT_STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    NOT_ENDS_WITH = "NOT_ENDS_WITH"
    REGEX = "REGEX"
    NOT_REGEX = "NOT_REGEX"


class DebugSrrMatcherRequestDtoResponseRulesRulesResponseType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    """{"errorMessage":"Invalid response type. Please select a valid response type.","markdownDescription":"Type of the response. Determines the type of **response** to be returned when the rule is matched.","markdownEnumDescriptions":["Return **subscription** in XRAY-JSON format. (Using `Xray Json` template)","Return **subscription** in BASE64 encoded string. Compatible with most client application with Xray core.","Return **subscription** in Mihomo format. (Using `Mihomo` template)","Return **subscription** in Stash format. (Using `Stash` template)","Return **subscription** in Clash format. (Using `Clash` template) Useful for client application that use Legacy Clash core.","Return **subscription** in Singbox format. (Using `Singbox` template) Format which is used by Singbox client application.","Return **subscription** as browser format. The same as on `/info` route.","**Drop** request and return `403` status code.","**Drop** request and return `404` status code.","**Drop** request and return `451` status code.","**Drop** the socket connection."]}"""

    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"
    BROWSER = "BROWSER"
    BLOCK = "BLOCK"
    STATUS_CODE_404 = "STATUS_CODE_404"
    STATUS_CODE_451 = "STATUS_CODE_451"
    SOCKET_DROP = "SOCKET_DROP"


class DebugSrrMatcherResponseDtoResponseResponseType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"
    BROWSER = "BROWSER"
    BLOCK = "BLOCK"
    STATUS_CODE_404 = "STATUS_CODE_404"
    STATUS_CODE_451 = "STATUS_CODE_451"
    SOCKET_DROP = "SOCKET_DROP"


class DropConnectionsRequestDtoDropByBy(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    USERUUIDS = "userUuids"


class DropConnectionsRequestDtoDropBy2By(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    IPADDRESSES = "ipAddresses"


class DropConnectionsRequestDtoTargetNodesTarget(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ALLNODES = "allNodes"


class DropConnectionsRequestDtoTargetNodes2Target(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    SPECIFICNODES = "specificNodes"


class GetAllSubscriptionsResponseDtoResponseSubscriptionsUserTrafficLimitStrategy(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class RequestDtoProvider(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"
    KEYCLOAK = "keycloak"
    GENERIC = "generic"


class RemnawaveWebhookCrmEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    CRM = "crm"


class RemnawaveWebhookCrmEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_7_DAYS = "crm.infra_billing_node_payment_in_7_days"
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_48HRS = "crm.infra_billing_node_payment_in_48hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_IN_24HRS = "crm.infra_billing_node_payment_in_24hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_DUE_TODAY = "crm.infra_billing_node_payment_due_today"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_24HRS = "crm.infra_billing_node_payment_overdue_24hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_48HRS = "crm.infra_billing_node_payment_overdue_48hrs"
    CRM_INFRA_BILLING_NODE_PAYMENT_OVERDUE_7_DAYS = "crm.infra_billing_node_payment_overdue_7_days"


class RemnawaveWebhookErrorsEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ERRORS = "errors"


class RemnawaveWebhookErrorsEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ERRORS_BANDWIDTH_USAGE_THRESHOLD_REACHED_MAX_NOTIFICATIONS = "errors.bandwidth_usage_threshold_reached_max_notifications"


class RemnawaveWebhookNodeEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    NODE = "node"


class RemnawaveWebhookNodeEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    NODE_CREATED = "node.created"
    NODE_MODIFIED = "node.modified"
    NODE_DISABLED = "node.disabled"
    NODE_ENABLED = "node.enabled"
    NODE_DELETED = "node.deleted"
    NODE_CONNECTION_LOST = "node.connection_lost"
    NODE_CONNECTION_RESTORED = "node.connection_restored"
    NODE_TRAFFIC_NOTIFY = "node.traffic_notify"


class RemnawaveWebhookServiceEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    SERVICE = "service"


class RemnawaveWebhookServiceEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    SERVICE_PANEL_STARTED = "service.panel_started"
    SERVICE_LOGIN_ATTEMPT_FAILED = "service.login_attempt_failed"
    SERVICE_LOGIN_ATTEMPT_SUCCESS = "service.login_attempt_success"
    SERVICE_SUBPAGE_CONFIG_CHANGED = "service.subpage_config_changed"


class RemnawaveWebhookServiceEventsDtoDataSubpageConfigAction(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class RemnawaveWebhookUserEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    USER = "user"


class RemnawaveWebhookUserEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
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


class RemnawaveWebhookUserHwidDevicesEventsDtoScope(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    USER_HWID_DEVICES = "user_hwid_devices"


class RemnawaveWebhookUserHwidDevicesEventsDtoEvent(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    USER_HWID_DEVICES_ADDED = "user_hwid_devices.added"
    USER_HWID_DEVICES_DELETED = "user_hwid_devices.deleted"


class UpdateUserRequestDtoStatus(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


class SubscriptionControllerGetSubscriptionByClientTypeClientType(msgspex.StrEnum, metaclass=msgspex.BaseEnumMeta):
    STASH = "stash"
    SINGBOX = "singbox"
    MIHOMO = "mihomo"
    JSON = "json"
    V2RAY_JSON = "v2ray-json"
    CLASH = "clash"


__all__ = (
    "BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes",
    "BulkNodesActionsRequestDtoAction",
    "CreateUserRequestDtoStatus",
    "DebugSrrMatcherRequestDtoResponseRulesRulesConditionsOperator",
    "DebugSrrMatcherRequestDtoResponseRulesRulesOperator",
    "DebugSrrMatcherRequestDtoResponseRulesRulesResponseType",
    "DebugSrrMatcherRequestDtoResponseRulesVersion",
    "DebugSrrMatcherResponseDtoResponseResponseType",
    "DropConnectionsRequestDtoDropBy2By",
    "DropConnectionsRequestDtoDropByBy",
    "DropConnectionsRequestDtoTargetNodes2Target",
    "DropConnectionsRequestDtoTargetNodesTarget",
    "GetAllSubscriptionsResponseDtoResponseSubscriptionsUserTrafficLimitStrategy",
    "HostRequestDtoAlpn",
    "HostRequestDtoFingerprint",
    "RemnawaveWebhookCrmEventsDtoEvent",
    "RemnawaveWebhookCrmEventsDtoScope",
    "RemnawaveWebhookErrorsEventsDtoEvent",
    "RemnawaveWebhookErrorsEventsDtoScope",
    "RemnawaveWebhookNodeEventsDtoEvent",
    "RemnawaveWebhookNodeEventsDtoScope",
    "RemnawaveWebhookServiceEventsDtoDataSubpageConfigAction",
    "RemnawaveWebhookServiceEventsDtoEvent",
    "RemnawaveWebhookServiceEventsDtoScope",
    "RemnawaveWebhookUserEventsDtoEvent",
    "RemnawaveWebhookUserEventsDtoScope",
    "RemnawaveWebhookUserHwidDevicesEventsDtoEvent",
    "RemnawaveWebhookUserHwidDevicesEventsDtoScope",
    "RequestDtoProvider",
    "SecurityLayer",
    "Status",
    "SubscriptionControllerGetSubscriptionByClientTypeClientType",
    "TrafficLimitStrategy",
    "TrafficLimitStrategy2",
    "UpdateUserRequestDtoStatus",
)
