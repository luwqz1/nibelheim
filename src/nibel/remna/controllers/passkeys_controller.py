import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import DeletePasskeyRequestDto, UpdatePasskeyRequestDto, VerifyPasskeyRegistrationRequestDto
from ..remnawave import remnawave
from ..responses import (
    DeletePasskeyResponseDto,
    GetAllPasskeysResponseDto,
    GetPasskeyRegistrationOptionsResponseDto,
    UpdatePasskeyResponseDto,
    VerifyPasskeyRegistrationResponseDto,
)

PASSKEYS_CONTROLLER_AUTH = Authorization


@remnawave("/passkeys", auth=PASSKEYS_CONTROLLER_AUTH)
class PasskeysController:
    @saronia.get("/registration/options")
    async def passkey_registration_options(
        self,
    ) -> saronia.APIResult[
        GetPasskeyRegistrationOptionsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/registration/verify", VerifyPasskeyRegistrationRequestDto)
    async def passkey_registration_verify(
        self,
    ) -> saronia.APIResult[
        VerifyPasskeyRegistrationResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_active_passkeys(
        self,
    ) -> saronia.APIResult[
        GetAllPasskeysResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/", DeletePasskeyRequestDto)
    async def delete_passkey(
        self,
    ) -> saronia.APIResult[
        DeletePasskeyResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdatePasskeyRequestDto)
    async def update_passkey(
        self,
    ) -> saronia.APIResult[
        UpdatePasskeyResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("PasskeysController",)
