from nibel.model.msgspec_utils.custom_types.enum import BaseEnumMeta, StrEnum


class ALPN(StrEnum, metaclass=BaseEnumMeta):
    """Application-Layer Protocol Negotiation."""

    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"


class ErrorCode(StrEnum, metaclass=BaseEnumMeta):
    """Error code of the API."""

    INTERNAL_SERVER_ERROR = "A001"
    """Server error."""

    LOGIN_ERROR = "A002"
    """Login error."""

    UNAUTHORIZED = "A003"
    """Unauthorized."""

    FORBIDDEN_ROLE_ERROR = "A004"
    """Forbidden role error."""

    CREATE_API_TOKEN_ERROR = "A005"
    """Create API token error."""

    DELETE_API_TOKEN_ERROR = "A006"
    """Delete API token error."""

    REQUESTED_TOKEN_NOT_FOUND = "A007"
    """Requested token not found."""

    FIND_ALL_API_TOKENS_ERROR = "A008"
    """Find all API tokens error."""

    GET_PUBLIC_KEY_ERROR = "A009"
    """Get public key error."""

    ENABLE_NODE_ERROR = "A010"
    """Enable node error."""

    NODE_NOT_FOUND = "A011"
    """Node not found."""

    CONFIG_NOT_FOUND = "A012"
    """Configuration not found."""

    UPDATE_CONFIG_ERROR = "A013"
    """Error updating configuration."""

    GET_CONFIG_ERROR = "A014"
    """Error retrieving configuration."""

    DELETE_MANY_INBOUNDS_ERROR = "A015"
    """Delete many inbounds error."""

    CREATE_MANY_INBOUNDS_ERROR = "A016"
    """Create many inbounds error."""

    FIND_ALL_INBOUNDS_ERROR = "A017"
    """Find all inbounds error."""

    CREATE_USER_ERROR = "A018"
    """Failed to create user."""

    USER_USERNAME_ALREADY_EXISTS = "A019"
    """User username already exists."""

    USER_SHORT_UUID_ALREADY_EXISTS = "A020"
    """User short UUID already exists."""

    USER_SUBSCRIPTION_UUID_ALREADY_EXISTS = "A021"
    """User subscription UUID already exists."""

    CREATE_USER_WITH_INBOUNDS_ERROR = "A022"
    """User creation successful, but inbound creation failed. User not created."""

    CANT_GET_CREATED_USER_WITH_INBOUNDS = "A023"
    """User creation successful, but failed to get created user with inbounds."""

    GET_ALL_USERS_ERROR = "A024"
    """Get all users error."""

    USER_NOT_FOUND = "A025"
    """User not found."""

    GET_USER_BY_ERROR = "A026"
    """Get user by error."""

    REVOKE_USER_SUBSCRIPTION_ERROR = "A027"
    """Revoke user subscription error."""

    DISABLE_USER_ERROR = "A028"
    """Disable user error."""

    USER_ALREADY_DISABLED = "A029"
    """User already disabled."""

    USER_ALREADY_ENABLED = "A030"
    """User already enabled."""

    ENABLE_USER_ERROR = "A031"
    """Enable user error."""

    CREATE_NODE_ERROR = "A032"
    """Create node error."""

    NODE_NAME_ALREADY_EXISTS = "A033"
    """Node name already exists."""

    NODE_ADDRESS_ALREADY_EXISTS = "A034"
    """Node address already exists."""

    RESTART_NODE_ERROR = "A035"
    """Restart node error."""

    GET_CONFIG_WITH_USERS_ERROR = "A036"
    """Get config with users error."""

    DELETE_USER_ERROR = "A037"
    """Delete user error."""

    UPDATE_NODE_ERROR = "A038"
    """Update node error."""

    UPDATE_USER_ERROR = "A039"
    """Update user error."""

    INCREMENT_USED_TRAFFIC_ERROR = "A040"
    """Increment used traffic error."""

    GET_ALL_NODES_ERROR = "A041"
    """Get all nodes error."""

    GET_ONE_NODE_ERROR = "A042"
    """Get one node error."""

    DELETE_NODE_ERROR = "A043"
    """Delete node error."""

    CREATE_HOST_ERROR = "A044"
    """Create host error."""

    HOST_REMARK_ALREADY_EXISTS = "A045"
    """Host remark already exists."""

    HOST_NOT_FOUND = "A046"
    """Host not found."""

    DELETE_HOST_ERROR = "A047"
    """Delete host error."""

    GET_USER_STATS_ERROR = "A048"
    """Get user stats error."""

    UPDATE_USER_WITH_INBOUNDS_ERROR = "A049"
    """Update user with inbounds error."""

    GET_ALL_HOSTS_ERROR = "A050"
    """Get all hosts error."""

    REORDER_HOSTS_ERROR = "A051"
    """Reorder hosts error."""

    UPDATE_HOST_ERROR = "A052"
    """Update host error."""

    CREATE_CONFIG_ERROR = "A053"
    """Create config error."""

    ENABLED_NODES_NOT_FOUND = "A054"
    """Enabled nodes not found."""

    GET_NODES_USAGE_BY_RANGE_ERROR = "A055"
    """Get nodes usage by range error."""

    RESET_USER_TRAFFIC_ERROR = "A056"
    """Reset user traffic error."""

    REORDER_NODES_ERROR = "A057"
    """Reorder nodes error."""

    GET_ALL_INBOUNDS_ERROR = "A058"
    """Get all inbounds error."""

    BULK_DELETE_USERS_BY_STATUS_ERROR = "A059"
    """Bulk delete users by status error."""

    UPDATE_INBOUND_ERROR = "A060"
    """Update inbound error."""

    CONFIG_VALIDATION_ERROR = "A061"
    """Config validation error."""

    USERS_NOT_FOUND = "A062"
    """Users not found."""

    GET_USER_BY_UNIQUE_FIELDS_NOT_FOUND = "A063"
    """User with specified params not found."""

    UPDATE_EXCEEDED_TRAFFIC_USERS_ERROR = "A064"
    """Update exceeded traffic users error."""

    ADMIN_NOT_FOUND = "A065"
    """Admin not found."""

    CREATE_ADMIN_ERROR = "A066"
    """Create admin error."""

    GET_AUTH_STATUS_ERROR = "A067"
    """Get auth status error."""

    FORBIDDEN = "A068"
    """Forbidden."""

    DISABLE_NODE_ERROR = "A069"
    """Disable node error."""

    GET_ONE_HOST_ERROR = "A070"
    """Get one host error."""

    SUBSCRIPTION_SETTINGS_NOT_FOUND = "A071"
    """Subscription settings not found."""

    GET_SUBSCRIPTION_SETTINGS_ERROR = "A072"
    """Get subscription settings error."""

    UPDATE_SUBSCRIPTION_SETTINGS_ERROR = "A073"
    """Update subscription settings error."""

    ADD_INBOUND_TO_USERS_ERROR = "A074"
    """Add inbound to users error."""

    REMOVE_INBOUND_FROM_USERS_ERROR = "A075"
    """Remove inbound from users error."""

    INBOUND_NOT_FOUND = "A076"
    """Inbound not found."""

    ADD_INBOUND_TO_NODES_ERROR = "A077"
    """Add inbound to nodes error."""

    REMOVE_INBOUND_FROM_NODES_ERROR = "A078"
    """Remove inbound from nodes error."""

    DELETE_HOSTS_ERROR = "A079"
    """Delete hosts error."""

    BULK_ENABLE_HOSTS_ERROR = "A080"
    """Bulk enable hosts error."""

    BULK_DISABLE_HOSTS_ERROR = "A081"
    """Bulk disable hosts error."""

    SET_INBOUND_TO_HOSTS_ERROR = "A082"
    """Set inbound to hosts error."""

    SET_PORT_TO_HOSTS_ERROR = "A083"
    """Set port to hosts error."""

    BULK_DELETE_USERS_BY_UUID_ERROR = "A084"
    """Bulk delete users by UUID error."""

    BULK_REVOKE_USERS_SUBSCRIPTION_ERROR = "A085"
    """Bulk revoke users subscription error."""

    BULK_RESET_USER_TRAFFIC_ERROR = "A086"
    """Bulk reset user traffic error."""

    BULK_UPDATE_USERS_ERROR = "A087"
    """Bulk update users error."""

    BULK_ADD_INBOUNDS_TO_USERS_ERROR = "A088"
    """Bulk add inbounds to users error."""

    BULK_UPDATE_ALL_USERS_ERROR = "A089"
    """Bulk update all users error."""

    INVALID_USER_STATUS_ERROR = "A089"
    """LIMITED and EXPIRED statuses are not allowed to be set manually."""

    KEYPAIR_CREATION_ERROR = "A090"
    """Keypair creation error."""

    GET_USER_USAGE_BY_RANGE_ERROR = "A091"
    """Get user usage by range error."""

    KEYPAIR_NOT_FOUND = "A092"
    """Keypair not found. Restart app."""

    ACTIVATE_ALL_INBOUNDS_ERROR = "A093"
    """Activate all inbounds error."""

    GET_NODES_USER_USAGE_BY_RANGE_ERROR = "A094"
    """Get nodes user usage by range error."""

    GET_NODES_REALTIME_USAGE_ERROR = "A095"
    """Get nodes realtime usage error."""

    CREATE_HWID_USER_DEVICE_ERROR = "A096"
    """Create hwid user device error."""

    CHECK_HWID_EXISTS_ERROR = "A097"
    """Check hwid exists error."""

    USER_HWID_DEVICE_ALREADY_EXISTS = "A098"
    """User hwid device already exists."""

    USER_HWID_DEVICE_LIMIT_REACHED = "A099"
    """User hwid device limit reached."""

    GET_USER_HWID_DEVICES_ERROR = "A100"
    """Get user hwid devices error."""

    DELETE_HWID_USER_DEVICE_ERROR = "A101"
    """Delete hwid user device error."""

    UPSERT_HWID_USER_DEVICE_ERROR = "A102"
    """Upsert hwid user device error."""

    GET_ALL_TAGS_ERROR = "A103"
    """Get all tags error."""

    GETTING_ALL_SUBSCRIPTIONS_ERROR = "A104"
    """Getting all subscriptions error."""

    TRIGGER_THRESHOLD_NOTIFICATION_ERROR = "A105"
    """Trigger threshold notification error."""

    BULK_DELETE_BY_STATUS_ERROR = "A106"
    """Bulk delete by status error."""

    CLEAN_OLD_USAGE_RECORDS_ERROR = "A107"
    """Clean old usage records error."""

    VACUUM_TABLE_ERROR = "A108"
    """Vacuum table error."""

    GET_CONFIG_PROFILES_ERROR = "A109"
    """Get config profiles error."""

    GET_CONFIG_PROFILE_BY_UUID_ERROR = "A110"
    """Get config profile by UUID error."""

    CONFIG_PROFILE_NOT_FOUND = "A111"
    """Config profile not found."""

    CREATE_CONFIG_PROFILE_ERROR = "A112"
    """Create config profile error."""

    INBOUNDS_WITH_SAME_TAG_ALREADY_EXISTS = "A113"
    """Inbounds with same tag already exists in database. Inbound tags must be
    unique."""

    CONFIG_PROFILE_NAME_ALREADY_EXISTS = "A114"
    """Config profile name already exists in database. Config profile names must
    be unique."""

    GET_INBOUNDS_BY_PROFILE_UUID_ERROR = "A115"
    """Get inbounds by profile UUID error."""

    GET_INTERNAL_SQUADS_ERROR = "A116"
    """Get internal squads error."""

    GET_INTERNAL_SQUAD_BY_UUID_ERROR = "A117"
    """Get internal squad by UUID error."""

    INTERNAL_SQUAD_NOT_FOUND = "A118"
    """Internal squad not found."""

    CREATE_INTERNAL_SQUAD_ERROR = "A119"
    """Create internal squad error."""

    INTERNAL_SQUAD_NAME_ALREADY_EXISTS = "A120"
    """Internal squad name already exists."""

    UPDATE_INTERNAL_SQUAD_ERROR = "A121"
    """Update internal squad error."""

    DELETE_INTERNAL_SQUAD_ERROR = "A122"
    """Delete internal squad error."""

    CREATE_USER_WITH_INTERNAL_SQUAD_ERROR = "A123"
    """Create user with internal squad error."""

    CONFIG_PROFILE_INBOUND_NOT_FOUND_IN_SPECIFIED_PROFILE = "A124"
    """Config profile inbound not found in specified profile."""

    GET_USER_ACCESSIBLE_NODES_ERROR = "A125"
    """Get user accessible nodes error."""

    GET_INFRA_PROVIDERS_ERROR = "A126"
    """Get infra providers error."""

    GET_INFRA_PROVIDER_BY_UUID_ERROR = "A127"
    """Get infra provider by UUID error."""

    INFRA_PROVIDER_NOT_FOUND = "A128"
    """Infra provider not found."""

    DELETE_INFRA_PROVIDER_BY_UUID_ERROR = "A129"
    """Delete infra provider by UUID error."""

    CREATE_INFRA_PROVIDER_ERROR = "A130"
    """Create infra provider error."""

    UPDATE_INFRA_PROVIDER_ERROR = "A131"
    """Update infra provider error."""

    CREATE_INFRA_BILLING_HISTORY_RECORD_ERROR = "A132"
    """Create infra billing history record error."""

    GET_INFRA_BILLING_HISTORY_RECORDS_ERROR = "A133"
    """Get infra billing history records error."""

    DELETE_INFRA_BILLING_HISTORY_RECORD_BY_UUID_ERROR = "A134"
    """Delete infra billing history record by UUID error."""

    GET_BILLING_NODES_ERROR = "A135"
    """Get billing nodes error."""

    UPDATE_INFRA_BILLING_NODE_ERROR = "A136"
    """Update infra billing node error."""

    CREATE_INFRA_BILLING_NODE_ERROR = "A137"
    """Create infra billing node error."""

    DELETE_INFRA_BILLING_NODE_BY_UUID_ERROR = "A138"
    """Delete infra billing node by UUID error."""

    GET_BILLING_NODES_FOR_NOTIFICATIONS_ERROR = "A139"
    """Get billing nodes for notifications error."""

    ADD_USERS_TO_INTERNAL_SQUAD_ERROR = "A140"
    """Add users to internal squad error."""

    INTERNAL_SQUAD_BULK_ACTIONS_ERROR = "A141"
    """Internal squad bulk actions error."""

    REMOVE_USERS_FROM_INTERNAL_SQUAD_ERROR = "A142"
    """Remove users from internal squad error."""

    DELETE_CONFIG_PROFILE_BY_UUID_ERROR = "A143"
    """Delete config profile by UUID error."""

    RESERVED_INTERNAL_SQUAD_NAME = "A144"
    """This name is reserved by Remnawave. Please use a different name."""

    RESERVED_CONFIG_PROFILE_NAME = "A145"
    """This name is reserved by Remnawave. Please use a different name."""

    UPDATE_CONFIG_PROFILE_ERROR = "A146"
    """Update config profile error."""

    OAUTH2_PROVIDER_NOT_FOUND = "A147"
    """OAuth2 provider not found."""

    OAUTH2_AUTHORIZE_ERROR = "A148"
    """OAuth2 authorize error."""

    NODE_IS_DISABLED = "A149"
    """Node is disabled."""

    SYNC_ACTIVE_PROFILE_ERROR = "A150"
    """Sync active profile error."""

    GET_ALL_HOST_TAGS_ERROR = "A151"
    """Get all host tags error."""

    NAME_OR_CONFIG_REQUIRED = "A152"
    """Name or config is required."""

    NAME_OR_INBOUNDS_REQUIRED = "A153"
    """Name or inbounds is required."""

    GET_INTERNAL_SQUAD_ACCESSIBLE_NODES_ERROR = "A154"
    """Get internal squad accessible nodes error."""

    DELETE_HWID_USER_DEVICES_ERROR = "A155"
    """Delete hwid user devices error."""

    CREATE_USER_SUBSCRIPTION_REQUEST_HISTORY_ERROR = "A156"
    """Create user subscription request history error."""

    GET_USER_SUBSCRIPTION_REQUEST_HISTORY_ERROR = "A157"
    """Get user subscription request history error."""

    GET_ALL_HWID_DEVICES_ERROR = "A158"
    """Get all hwid devices error."""

    GET_HWID_DEVICES_STATS_ERROR = "A159"
    """Get hwid devices stats error."""

    GET_USER_SUBSCRIPTION_REQUEST_HISTORY_STATS_ERROR = "A160"
    """Get user subscription request history stats error."""

    GET_SNIPPETS_ERROR = "A161"
    """Get snippets error."""

    SNIPPET_NOT_FOUND = "A162"
    """Snippet not found."""

    DELETE_SNIPPET_BY_NAME_ERROR = "A163"
    """Delete snippet by name error."""

    SNIPPET_NAME_ALREADY_EXISTS = "A164"
    """Snippet name already exists."""

    UPDATE_SNIPPET_ERROR = "A165"
    """Update snippet error."""

    SNIPPET_CANNOT_BE_EMPTY = "A166"
    """Snippet cannot be empty."""

    SNIPPET_CANNOT_CONTAIN_EMPTY_OBJECTS = "A167"
    """Snippet cannot contain empty objects."""

    GET_ALL_SUBSCRIPTION_TEMPLATES_ERROR = "A168"
    """Get all subscription templates error."""

    GET_SUBSCRIPTION_TEMPLATE_BY_UUID_ERROR = "A169"
    """Get subscription template by UUID error."""

    SUBSCRIPTION_TEMPLATE_NOT_FOUND = "A170"
    """Subscription template not found."""

    UPDATE_SUBSCRIPTION_TEMPLATE_ERROR = "A171"
    """Update subscription template error."""

    RESERVED_TEMPLATE_NAME = "A172"
    """This name is reserved. Please use a different name."""

    TEMPLATE_JSON_NOT_ALLOWED_FOR_YAML_TEMPLATE = "A173"
    """Template JSON is not allowed for YAML template."""

    TEMPLATE_YAML_NOT_ALLOWED_FOR_JSON_TEMPLATE = "A174"
    """Template YAML is not allowed for JSON template."""

    TEMPLATE_JSON_AND_YAML_CANNOT_BE_UPDATED_SIMULTANEOUSLY = "A175"
    """Template JSON and YAML cannot be updated simultaneously."""

    TEMPLATE_NAME_ALREADY_EXISTS_FOR_THIS_TYPE = "A176"
    """Template name already exists for this type."""

    DELETE_SUBSCRIPTION_TEMPLATE_ERROR = "A177"
    """Delete subscription template error."""

    RESERVED_TEMPLATE_CANNOT_BE_DELETED = "A178"
    """Reserved template cannot be deleted."""

    CREATE_SUBSCRIPTION_TEMPLATE_ERROR = "A179"
    """Create subscription template error."""

    TEMPLATE_TYPE_NOT_ALLOWED = "A180"
    """Template type not allowed."""

    GET_EXTERNAL_SQUADS_ERROR = "A181"
    """Get external squads error."""

    EXTERNAL_SQUAD_NOT_FOUND = "A182"
    """External squad not found."""

    CREATE_EXTERNAL_SQUAD_ERROR = "A183"
    """Create external squad error."""

    UPDATE_EXTERNAL_SQUAD_ERROR = "A184"
    """Update external squad error."""

    DELETE_EXTERNAL_SQUAD_ERROR = "A185"
    """Delete external squad error."""

    ADD_USERS_TO_EXTERNAL_SQUAD_ERROR = "A186"
    """Add users to external squad error."""

    REMOVE_USERS_FROM_EXTERNAL_SQUAD_ERROR = "A187"
    """Remove users from external squad error."""

    GET_EXTERNAL_SQUAD_BY_UUID_ERROR = "A188"
    """Get external squad by UUID error."""

    EXTERNAL_SQUAD_NAME_ALREADY_EXISTS = "A189"
    """External squad name already exists."""

    NAME_OR_TEMPLATES_REQUIRED = "A190"
    """Name or templates are required."""

    PASSKEY_NOT_FOUND = "A191"
    """Passkey not found."""

    GET_REMNAAWAVE_SETTINGS_ERROR = "A192"
    """Get Remnawave settings error."""

    UPDATE_REMNAAWAVE_SETTINGS_ERROR = "A193"
    """Update Remnawave settings error."""

    PASSKEYS_NOT_CONFIGURED = "A194"
    """Passkeys not configured."""

    PASSKEYS_NOT_ENABLED = "A195"
    """Passkeys not enabled. Please enable it first."""

    GENERATE_PASSKEY_REGISTRATION_OPTIONS = "A196"
    """Generate passkey registration options error."""

    VERIFY_PASSKEY_REGISTRATION_ERROR = "A197"
    """Verify passkey registration error."""

    GET_ACTIVE_PASSKEYS_ERROR = "A198"
    """Get active passkeys error."""

    VALIDATE_REMNAAWAVE_SETTINGS_ERROR = "A199"
    """Validate Remnawave settings error."""

    DELETE_PASSKEY_ERROR = "A199"
    """Delete passkey error."""

    GET_COMPUTED_CONFIG_PROFILE_BY_UUID_ERROR = "A200"
    """Get computed config profile by UUID error."""

    RESET_NODE_TRAFFIC_ERROR = "A201"
    """Reset node traffic error."""

    UPDATE_PASSKEY_ERROR = "A202"
    """Update passkey error."""

    GENERIC_REORDER_ERROR = "A203"
    """Generic reorder error."""

    HWID_DEVICE_NOT_FOUND = "A204"
    """HWID device not found."""

    BULK_EXTEND_EXPIRATION_DATE_ERROR = "A205"
    """Bulk extend expiration date error."""

    SUBSCRIPTION_PAGE_CONFIG_NOT_FOUND = "A206"
    """Subscription page config not found."""

    GET_SUBSCRIPTION_PAGE_CONFIG_BY_UUID_ERROR = "A207"
    """Get subscription page config by UUID error."""

    GET_ALL_SUBSCRIPTION_PAGE_CONFIGS_ERROR = "A208"
    """Get all subscription page configs error."""

    RESERVED_CONFIG_NAME = "A209"
    """Reserved config name."""

    CONFIG_NAME_ALREADY_EXISTS = "A210"
    """Config name already exists."""

    UPDATE_SUBSCRIPTION_PAGE_CONFIG_ERROR = "A211"
    """Update subscription page config error."""

    RESERVED_SUBPAGE_CONFIG_CANT_BE_DELETED = "A212"
    """Reserved subpage config cannot be deleted."""

    DELETE_SUBSCRIPTION_PAGE_CONFIG_ERROR = "A213"
    """Delete subscription page config error."""

    CREATE_SUBSCRIPTION_PAGE_CONFIG_ERROR = "A214"
    """Create subscription page config error."""

    INVALID_SUBSCRIPTION_PAGE_CONFIG = "A215"
    """Invalid subscription page config."""


class ClientType(StrEnum, metaclass=BaseEnumMeta):
    """Client type of subscription."""

    STASH = "stash"
    SINGBOX = "singbox"
    MIHOMO = "mihomo"
    JSON = "json"
    V2RAY_JSON = "v2ray-json"
    CLASH = "clash"


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


class Operator(StrEnum, metaclass=BaseEnumMeta):
    """Operator to use for combining conditions in the rule."""

    AND = "AND"
    OR = "OR"
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


class Provider(StrEnum, metaclass=BaseEnumMeta):
    """OAuth2 authorization provider."""

    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"


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


class TemplateType(StrEnum, metaclass=BaseEnumMeta):
    """Type of template configuration for `Xray-Core`, `mihomo`, etc."""

    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class TrafficLimitStrategy(StrEnum, metaclass=BaseEnumMeta):
    """Available reset periods."""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class Version(StrEnum, metaclass=BaseEnumMeta):
    """Response Rules Config Version."""

    V1 = "1"


__all__ = (
    "ALPN",
    "ClientType",
    "ErrorCode",
    "Fingerprint",
    "Operator",
    "Provider",
    "ResponseType",
    "SecurityLayer",
    "Status",
    "TemplateType",
    "TrafficLimitStrategy",
    "Version",
)
