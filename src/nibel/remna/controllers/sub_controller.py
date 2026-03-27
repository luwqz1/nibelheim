import typing

import saronia

from ..errors import BadRequestError, InternalServerError
from ..objects import GetAllSubscriptionsResponseDtoResponseSubscriptions
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
        BadRequestError | InternalServerError,
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
    ) -> saronia.APIResult[GetAllSubscriptionsResponseDtoResponseSubscriptions]:
        """Args:
        short_uuid: Short UUID of the user

        """
        ...

    @saronia.get("/{shortUuid}/{clientType}", form=GetPublicSubscriptionControllerSubscriptionByClientTypeSignature)
    async def get_subscription_by_client_type(self) -> saronia.APIResult[str]: ...

    @saronia.get("/outline/{shortUuid}/{type}/{encodedTag}")
    async def get_subscription_with_type(
        self,
        *,
        type: str,
        encoded_tag: saronia.Param[str, saronia.Path, "encodedTag"],
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
    ) -> saronia.APIResult[typing.Any]:
        """Args:
        type: Subscription type (required if encodedTag is provided). Only SS is supported for now.
        encoded_tag: Base64 encoded tag for Outline config. This paramter is optional. It is required only when type=ss.
        short_uuid: Short UUID of the user

        """
        ...


__all__ = ("SubController",)
