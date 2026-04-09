import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import UpdateSubscriptionSettingsRequestDto
from ..remnawave import remnawave
from ..responses import GetSubscriptionSettingsResponseDto, UpdateSubscriptionSettingsResponseDto

SUBSCRIPTION_SETTINGS_CONTROLLER_AUTH = Authorization


@remnawave("/subscription-settings", auth=SUBSCRIPTION_SETTINGS_CONTROLLER_AUTH)
class SubscriptionSettingsController:
    @saronia.get("/")
    async def get_settings(
        self,
    ) -> saronia.APIResult[
        GetSubscriptionSettingsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateSubscriptionSettingsRequestDto)
    async def update_settings(
        self,
    ) -> saronia.APIResult[
        UpdateSubscriptionSettingsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("SubscriptionSettingsController",)
