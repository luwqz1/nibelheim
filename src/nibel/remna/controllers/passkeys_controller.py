import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
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
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/registration/verify", form=VerifyPasskeyRegistrationRequestDto)
    async def passkey_registration_verify(
        self,
    ) -> saronia.APIResult[
        VerifyPasskeyRegistrationResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_active_passkeys(
        self,
    ) -> saronia.APIResult[
        GetAllPasskeysResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.delete("/", form=DeletePasskeyRequestDto)
    async def delete_passkey(
        self,
    ) -> saronia.APIResult[
        DeletePasskeyResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdatePasskeyRequestDto)
    async def update_passkey(
        self,
    ) -> saronia.APIResult[
        UpdatePasskeyResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("PasskeysController",)
