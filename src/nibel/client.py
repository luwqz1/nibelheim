import datetime
import pathlib
import typing

import certifi
from saronia.client.wreq_client import WreqClient
from wreq.dns import DnsOptions
from wreq.emulation import Emulation, Platform
from wreq.wreq import Client

from nibel.__meta__ import __version__
from nibel.remna import remnawave
from nibel.remna.auth import Authorization, Prometheus
from nibel.remna.controllers import APIControllers

NIBEL_USERAGENT: typing.Final = f"Nibelheim/{__version__}"
TIMEOUT: typing.Final = 60.0
POOL_IDLE_TIMEOUT: typing.Final = datetime.timedelta(seconds=60.0)
POOL_MAX_IDLE_PER_HOST: typing.Final = 32
POOL_MAX_SIZE: typing.Final = POOL_MAX_IDLE_PER_HOST * 2
TCP_KEEPALIVE: typing.Final = datetime.timedelta(seconds=60.0)
TCP_KEEPALIVE_INTERVAL = datetime.timedelta(seconds=15.0)
TCP_KEEPALIVE_RETRIES: typing.Final = 4
TCP_USER_TIMEOUT: typing.Final = (TCP_KEEPALIVE + TCP_KEEPALIVE_INTERVAL) * TCP_KEEPALIVE_RETRIES


class ClientSettings(typing.TypedDict):
    cookies: typing.NotRequired[typing.Mapping[str, str]]
    headers: typing.NotRequired[typing.Mapping[str, str]]
    tls_verify: typing.NotRequired[bool]
    read_timeout: typing.NotRequired[float]
    connect_timeout: typing.NotRequired[float]
    request_timeout: typing.NotRequired[float]


class Remnawave(APIControllers):
    @typing.overload
    def __init__(self, *, panel_url: str) -> None: ...

    @typing.overload
    def __init__(self, *, panel_url: str, http_client: Client) -> None: ...

    @typing.overload
    def __init__(self, *, panel_url: str, **settings: typing.Unpack[ClientSettings]) -> None: ...

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        http_client: Client,
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        **settings: typing.Unpack[ClientSettings],
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        username: str,
        password: str,
        http_client: Client,
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        username: str,
        password: str,
        **settings: typing.Unpack[ClientSettings],
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        username: str,
        password: str,
        http_client: Client,
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        username: str,
        password: str,
        **settings: typing.Unpack[ClientSettings],
    ) -> None:
        pass

    def __init__(
        self,
        *,
        panel_url: str,
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        http_client: Client | None = None,
        **settings: typing.Unpack[ClientSettings],
    ) -> None:
        self.panel_url = panel_url.removesuffix("/api")
        self.http = http_client or Client(
            dns_options=DnsOptions(system_dns=True),
            emulation=Emulation(
                profile=Emulation.Chrome147,
                platform=Platform.Linux,
                http2=True,
                headers=True,
            ),
            tcp_reuse_address=True,
            zstd=True,
            gzip=True,
            http2_only=True,
            tls_verify=False if settings.get("tls_verify", True) is False else pathlib.Path(certifi.where()),
            tcp_keepalive=TCP_KEEPALIVE,
            tcp_keepalive_interval=TCP_KEEPALIVE_INTERVAL,
            tcp_keepalive_retries=TCP_KEEPALIVE_RETRIES,
            tcp_user_timeout=TCP_USER_TIMEOUT,
            pool_max_size=POOL_MAX_SIZE,
            pool_idle_timeout=POOL_IDLE_TIMEOUT,
            pool_max_idle_per_host=POOL_MAX_IDLE_PER_HOST,
            connect_timeout=datetime.timedelta(seconds=settings.get("connect_timeout", TIMEOUT)),
            read_timeout=datetime.timedelta(seconds=settings.get("read_timeout", TIMEOUT)),
        )
        self.client = WreqClient(
            client=self.http,
            base_url=self.panel_url,
            user_agent=NIBEL_USERAGENT,
            request_timeout=settings.get("request_timeout", TIMEOUT),
            default_headers=True,
        )
        self.client.cookies.update(settings.get("cookies", {}))
        self.client.headers.update(settings.get("headers", {}))

        super().__init__(self.client)

        remnawave.auth(
            authorization=Authorization(token) if token else None,
            prometheus=Prometheus(username, password) if username and password else None,
        )

    def __repr__(self) -> str:
        return f"<Remnawave `{self.panel_url}`>"


__all__ = ("Remnawave",)
