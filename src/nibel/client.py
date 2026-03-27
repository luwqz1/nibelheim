import datetime
import pathlib
import typing

import certifi
import rnet
from saronia.client.base import DEFAULT_TIMEOUT, DEFAULT_USER_AGENT
from saronia.client.rnet_client import RnetClient

from nibel.__meta__ import __version__
from nibel.remna import remnawave
from nibel.remna.auth import Authorization, Prometheus
from nibel.remna.controllers import APIControllers

NIBEL_CLIENT_VERSION: typing.Final = f"rnet/3; Nibelheim/{__version__}"
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
    verify_ssl: typing.NotRequired[bool]
    read_timeout: typing.NotRequired[float]
    connect_timeout: typing.NotRequired[float]
    request_timeout: typing.NotRequired[float]


class Remnawave(APIControllers):
    @typing.overload
    def __init__(self, *, panel_url: str, **kwargs: typing.Unpack[ClientSettings]) -> None: ...

    @typing.overload
    def __init__(self, *, panel_url: str, http_client: rnet.Client) -> None: ...

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        **kwargs: typing.Unpack[ClientSettings],
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        token: str,
        http_client: rnet.Client,
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        username: str,
        password: str,
        **kwargs: typing.Unpack[ClientSettings],
    ) -> None:
        pass

    @typing.overload
    def __init__(
        self,
        *,
        panel_url: str,
        username: str,
        password: str,
        http_client: rnet.Client,
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
        **kwargs: typing.Unpack[ClientSettings],
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
        http_client: rnet.Client,
    ) -> None:
        pass

    def __init__(
        self,
        *,
        panel_url: str,
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        http_client: rnet.Client | None = None,
        **kwargs: typing.Unpack[ClientSettings],
    ) -> None:
        self.http = http_client or rnet.Client(
            emulation=rnet.EmulationOption(
                emulation=rnet.Emulation.Chrome145,
                emulation_os=rnet.EmulationOS.Linux,
                skip_http2=False,
                skip_headers=False,
            ),
            tcp_reuse_address=True,
            zstd=True,
            gzip=True,
            http2_only=True,
            verify=False if kwargs.get("verify_ssl", True) is False else pathlib.Path(certifi.where()),
            tcp_keepalive=TCP_KEEPALIVE,
            tcp_keepalive_interval=TCP_KEEPALIVE_INTERVAL,
            tcp_keepalive_retries=TCP_KEEPALIVE_RETRIES,
            tcp_user_timeout=TCP_USER_TIMEOUT,
            pool_max_size=POOL_MAX_SIZE,
            pool_idle_timeout=POOL_IDLE_TIMEOUT,
            pool_max_idle_per_host=POOL_MAX_IDLE_PER_HOST,
            connect_timeout=datetime.timedelta(seconds=kwargs.get("connect_timeout", DEFAULT_TIMEOUT)),
            read_timeout=datetime.timedelta(seconds=kwargs.get("read_timeout", DEFAULT_TIMEOUT)),
        )
        self.client = RnetClient(
            client=self.http,
            base_url=panel_url.removesuffix("/api"),
            user_agent=DEFAULT_USER_AGENT.format(http_client=NIBEL_CLIENT_VERSION),
            request_timeout=kwargs.get("request_timeout", DEFAULT_TIMEOUT),
            default_headers=True,
        )
        self.client.cookies.update(kwargs.get("cookies", {}))
        self.client.headers.update(kwargs.get("headers", {}))

        super().__init__(self.client)
        remnawave.auth(
            authorization=Authorization(token) if token else None,
            prometheus=Prometheus(username, password) if username and password else None,
        )


__all__ = ("Remnawave",)
