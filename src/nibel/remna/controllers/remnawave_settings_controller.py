import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
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
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateRemnawaveSettingsRequestDto)
    async def update_settings(
        self,
    ) -> saronia.APIResult[
        UpdateRemnawaveSettingsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("RemnawaveSettingsController",)
