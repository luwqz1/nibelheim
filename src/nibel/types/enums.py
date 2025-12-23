import enum


class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value


class Provider(StrEnum):
    GITHUB = "GITHUB"
    POCKETID = "POCKETID"
    YANDEX = "YANDEX"


class Status(StrEnum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class TrafficLimitStrategy(StrEnum):
    NORESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class TemplateType(StrEnum):
    XRAYJSON = "XRAY_JSON"
    XRAYBASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"


class Alpn(StrEnum):
    H3 = "H3"
    H2 = "H2"
    HTTP11 = "HTTP_1_1"
    HCOMBINED = "H_COMBINED"
    H3H2H1COMBINED = "H3_H2_H1_COMBINED"
    H3H2COMBINED = "H3_H2_COMBINED"


class Fingerprint(StrEnum):
    CHROME = "CHROME"
    FIREFOX = "FIREFOX"
    SAFARI = "SAFARI"
    IOS = "IOS"
    ANDROID = "ANDROID"
    EDGE = "EDGE"
    QQ = "QQ"
    RANDOM = "RANDOM"
    RANDOMIZED = "RANDOMIZED"


class SecurityLayer(StrEnum):
    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"


__all__ = ("Alpn", "Fingerprint", "Provider", "SecurityLayer", "Status", "TemplateType", "TrafficLimitStrategy")
