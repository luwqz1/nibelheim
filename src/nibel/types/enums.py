import enum


class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value


class Provider(StrEnum):
    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"


class Status(StrEnum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy(StrEnum):
    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class TemplateType(StrEnum):
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class Alpn(StrEnum):
    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"


class Fingerprint(StrEnum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"


class SecurityLayer(StrEnum):
    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"


__all__ = ("Alpn", "Fingerprint", "Provider", "SecurityLayer", "Status", "TemplateType", "TrafficLimitStrategy")
