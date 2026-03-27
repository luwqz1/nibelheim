import saronia

from ..errors import AuthControllerAuthError, BadRequestError, InternalServerError
from ..objects import (
    LoginRequestDto,
    OAuth2AuthorizeRequestDto,
    OAuth2CallbackRequestDto,
    RegisterRequestDto,
    TelegramCallbackRequestDto,
    VerifyPasskeyAuthenticationRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    GetPasskeyAuthenticationOptionsResponseDto,
    GetStatusResponseDto,
    LoginResponseDto,
    OAuth2AuthorizeResponseDto,
    OAuth2CallbackResponseDto,
    RegisterResponseDto,
    TelegramCallbackResponseDto,
    VerifyPasskeyAuthenticationResponseDto,
)


@remnawave("/auth")
class AuthController:
    @saronia.post("/login", form=LoginRequestDto)
    async def login(
        self,
    ) -> saronia.APIResult[
        LoginResponseDto,
        BadRequestError | AuthControllerAuthError | InternalServerError,
    ]: ...

    @saronia.post("/register", form=RegisterRequestDto)
    async def register(
        self,
    ) -> saronia.APIResult[
        RegisterResponseDto,
        BadRequestError | AuthControllerAuthError | InternalServerError,
    ]: ...

    @saronia.get("/status")
    async def get_status(
        self,
    ) -> saronia.APIResult[
        GetStatusResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/oauth2/tg/callback", form=TelegramCallbackRequestDto)
    async def telegram_callback(
        self,
    ) -> saronia.APIResult[
        TelegramCallbackResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/oauth2/authorize", form=OAuth2AuthorizeRequestDto)
    async def oauth2_authorize(
        self,
    ) -> saronia.APIResult[
        OAuth2AuthorizeResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/oauth2/callback", form=OAuth2CallbackRequestDto)
    async def oauth2_callback(
        self,
    ) -> saronia.APIResult[
        OAuth2CallbackResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/passkey/authentication/options")
    async def passkey_authentication_options(
        self,
    ) -> saronia.APIResult[
        GetPasskeyAuthenticationOptionsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/passkey/authentication/verify", form=VerifyPasskeyAuthenticationRequestDto)
    async def passkey_authentication_verify(
        self,
    ) -> saronia.APIResult[
        VerifyPasskeyAuthenticationResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("AuthController",)
