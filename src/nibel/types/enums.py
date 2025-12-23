import enum


class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value


class Provider(StrEnum):
    """OAuth2 authorization provider."""

    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"


class Status(StrEnum):
    """User account status."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy(StrEnum):
    """Available reset periods."""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class TemplateType(StrEnum):
    """Type of template configuration for `Xray-Core`, `mihomo`, etc."""

    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class ALPN(StrEnum):
    """Application-Layer Protocol Negotiation."""

    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"


class Fingerprint(StrEnum):
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


class SecurityLayer(StrEnum):
    """Transport layer encryption."""

    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"


__all__ = ("ALPN", "Fingerprint", "Provider", "SecurityLayer", "Status", "TemplateType", "TrafficLimitStrategy")
