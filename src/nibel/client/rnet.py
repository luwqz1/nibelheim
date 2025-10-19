import sys
import typing

import msgspec
import rnet

from nibel.__meta__ import __version__
from nibel.client.abc import ABCClient

type Method = typing.Literal["GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH"]

_METHODS_MAP: typing.Final = {
    "GET": rnet.Method.GET,
    "HEAD": rnet.Method.HEAD,
    "POST": rnet.Method.POST,
    "PUT": rnet.Method.PUT,
    "DELETE": rnet.Method.DELETE,
    "OPTIONS": rnet.Method.OPTIONS,
    "TRACE": rnet.Method.TRACE,
    "PATCH": rnet.Method.PATCH,
}
USER_AGENT: typing.Final = "Python/{}.{} rnet/2 Nibelheim/{}".format(
    sys.version_info.major,
    sys.version_info.minor,
    __version__,
)
DEFAULT_CONNECTION_TIMEOUT: typing.Final = 30
DEFAULT_READ_TIMEOUT: typing.Final = 30
DEFAULT_TIMEOUT: typing.Final = 30
DEFAULT_HTTP2_MAX_RETRIES: typing.Final = 10


class RnetClient(ABCClient):
    __slots__ = ("_timeout", "_client")

    def __init__(
        self,
        *,
        brotli: bool = True,
        zstd: bool = True,
        gzip: bool = True,
        proxies: list[rnet.Proxy] | None = None,
        timeout: int = DEFAULT_TIMEOUT,
        read_timeout: int = DEFAULT_READ_TIMEOUT,
        connect_timeout: int = DEFAULT_CONNECTION_TIMEOUT,
        http2_max_retries: int = DEFAULT_HTTP2_MAX_RETRIES,
        **client_kwargs: typing.Any,
    ) -> None:
        self._timeout = timeout
        self._client = rnet.Client(
            http2_only=True,
            user_agent=USER_AGENT,
            proxies=proxies,
            http2_max_retry_count=DEFAULT_HTTP2_MAX_RETRIES,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            timeout=timeout,
            allow_redirects=True,
            verify=True,
            brotli=brotli,
            zstd=zstd,
            gzip=gzip,
            **client_kwargs,
        )

    def __repr__(self) -> str:
        return "<{}: client={!r}, timeout={}>".format(
            type(self).__name__,
            self._client,
            self._timeout,
        )

    @property
    def timeout(self) -> float:
        return self._timeout

    async def close(self) -> None:
        pass

    async def request(
        self,
        url: str,
        method: Method,
        **kwargs: typing.Unpack[rnet.RequestParams],
    ) -> rnet.Response:
        return await self._client.request(_METHODS_MAP[method.upper()], url, **kwargs)

    async def request_text(
        self,
        *,
        url: str,
        method: Method = "GET",
        **kwargs: typing.Unpack[rnet.RequestParams],
    ) -> str:
        return await (await self.request(url, method, **kwargs)).text_with_charset(encoding="utf-8")

    async def request_bytes(
        self,
        *,
        url: str,
        method: Method = "GET",
        **kwargs: typing.Unpack[rnet.RequestParams],
    ) -> bytes:
        return await (await self.request(url, method, **kwargs)).bytes()

    async def request_content(
        self,
        *,
        url: str,
        method: Method = "GET",
        **kwargs: typing.Unpack[rnet.RequestParams],
    ) -> bytes:
        return await self.request_bytes(url=url, method=method, **kwargs)

    async def request_json(
        self,
        *,
        url: str,
        method: Method = "GET",
        **kwargs: typing.Unpack[rnet.RequestParams],
    ) -> dict[str, typing.Any]:
        return msgspec.json.decode(await self.request_bytes(url=url, method=method, **kwargs))


__all__ = ("RnetClient",)
