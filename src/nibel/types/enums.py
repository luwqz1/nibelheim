from nibel.model.msgspec_utils.custom_types.enum import BaseEnumMeta, StrEnum


class ALPN(StrEnum, metaclass=BaseEnumMeta):
    """Application-Layer Protocol Negotiation."""

    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"


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
