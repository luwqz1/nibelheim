import saronia

from ..errors import BadRequestError, NotFoundInternalServerError
from ..remnawave import remnawave
from ..responses import GetSubscriptionInfoResponseDto
from ..signatures import GetPublicSubscriptionControllerSubscriptionByClientTypeSignature


@remnawave("/sub")
class SubController:
    @saronia.get("/{shortUuid}/info")
    async def get_subscription_info_by_short_uuid(
        self,
        *,
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
    ) -> saronia.APIResult[
        GetSubscriptionInfoResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        short_uuid: Short UUID of the user

        """
        ...

    @saronia.get("/{shortUuid}")
    async def get_subscription(
        self,
        *,
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
    ) -> saronia.APIResult[None]:
        """Args:
        short_uuid: Short UUID of the user

        """
        ...

    @saronia.get("/{shortUuid}/{clientType}", GetPublicSubscriptionControllerSubscriptionByClientTypeSignature)
    async def get_subscription_by_client_type(self) -> saronia.APIResult[None]: ...


__all__ = ("SubController",)
