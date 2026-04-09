import saronia

from ..errors import AuthControllerAuthError, BadRequestError, NotFoundInternalServerError
from ..objects import LoginRequestDto, OAuth2AuthorizeRequestDto, OAuth2CallbackRequestDto, RegisterRequestDto, VerifyPasskeyAuthenticationRequestDto
from ..remnawave import remnawave
from ..responses import (
    GetPasskeyAuthenticationOptionsResponseDto,
    GetStatusResponseDto,
    LoginResponseDto,
    OAuth2AuthorizeResponseDto,
    OAuth2CallbackResponseDto,
    RegisterResponseDto,
    VerifyPasskeyAuthenticationResponseDto,
)


@remnawave("/auth")
class AuthController:
    @saronia.post("/login", LoginRequestDto)
    async def login(
        self,
    ) -> saronia.APIResult[
        LoginResponseDto,
        BadRequestError | AuthControllerAuthError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/register", RegisterRequestDto)
    async def register(
        self,
    ) -> saronia.APIResult[
        RegisterResponseDto,
        BadRequestError | AuthControllerAuthError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/status")
    async def get_status(
        self,
    ) -> saronia.APIResult[
        GetStatusResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/oauth2/authorize", OAuth2AuthorizeRequestDto)
    async def oauth2_authorize(
        self,
    ) -> saronia.APIResult[
        OAuth2AuthorizeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/oauth2/callback", OAuth2CallbackRequestDto)
    async def oauth2_callback(
        self,
    ) -> saronia.APIResult[
        OAuth2CallbackResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/passkey/authentication/options")
    async def passkey_authentication_options(
        self,
    ) -> saronia.APIResult[
        GetPasskeyAuthenticationOptionsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/passkey/authentication/verify", VerifyPasskeyAuthenticationRequestDto)
    async def passkey_authentication_verify(
        self,
    ) -> saronia.APIResult[
        VerifyPasskeyAuthenticationResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("AuthController",)
