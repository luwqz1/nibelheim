import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import UpdateRemnawaveSettingsRequestDto
from ..remnawave import remnawave
from ..responses import GetRemnawaveSettingsResponseDto, UpdateRemnawaveSettingsResponseDto

REMNAWAVE_SETTINGS_CONTROLLER_AUTH = Authorization


@remnawave("/remnawave-settings", auth=REMNAWAVE_SETTINGS_CONTROLLER_AUTH)
class RemnawaveSettingsController:
    @saronia.get("/")
    async def get_settings(
        self,
    ) -> saronia.APIResult[
        GetRemnawaveSettingsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateRemnawaveSettingsRequestDto)
    async def update_settings(
        self,
    ) -> saronia.APIResult[
        UpdateRemnawaveSettingsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("RemnawaveSettingsController",)
