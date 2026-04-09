from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError, SubscriptionsControllerNotFoundError
from ..remnawave import remnawave
from ..responses import (
    GetAllSubscriptionsResponseDto,
    GetConnectionKeysByUuidResponseDto,
    GetRawSubscriptionByShortUuidResponseDto,
    GetSubpageConfigByShortUuidResponseDto,
    GetSubscriptionByShortUuidProtectedResponseDto,
    GetSubscriptionByUsernameResponseDto,
    GetSubscriptionByUuidResponseDto,
)
from ..signatures import GetProtectedSubscriptionsControllerSubpageConfigByShortUuidSignature

PROTECTED_SUBSCRIPTIONS_CONTROLLER_AUTH = Authorization


@remnawave("/subscriptions", auth=PROTECTED_SUBSCRIPTIONS_CONTROLLER_AUTH)
class SubscriptionsController:
    @saronia.get("/", query=True)
    async def get_all_subscriptions(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetAllSubscriptionsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        size: Number of subscriptions to return, no more than 500
        start: Start index (offset) of the users to return, default is 0

        """
        ...

    @saronia.get("/by-username/{username}")
    async def get_subscription_by_username(
        self,
        *,
        username: str,
    ) -> saronia.APIResult[
        GetSubscriptionByUsernameResponseDto,
        BadRequestError | SubscriptionsControllerNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        username: Username of the user

        """
        ...

    @saronia.get("/by-short-uuid/{shortUuid}")
    async def get_subscription_by_short_uuid_protected(
        self,
        *,
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
    ) -> saronia.APIResult[
        GetSubscriptionByShortUuidProtectedResponseDto,
        BadRequestError | SubscriptionsControllerNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        short_uuid: Short uuid of the user

        """
        ...

    @saronia.get("/by-uuid/{uuid}")
    async def get_subscription_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetSubscriptionByUuidResponseDto,
        BadRequestError | SubscriptionsControllerNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: Uuid of the user

        """
        ...

    @saronia.get("/by-short-uuid/{shortUuid}/raw")
    async def get_raw_subscription_by_short_uuid(
        self,
        *,
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
        with_disabled_hosts: saronia.Param[bool | None, saronia.Query, "withDisabledHosts"] = None,
    ) -> saronia.APIResult[
        GetRawSubscriptionByShortUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        short_uuid: Short UUID of the user
        with_disabled_hosts: Include disabled hosts in the subscription. Default is false.

        """
        ...

    @saronia.get("/subpage-config/{shortUuid}", GetProtectedSubscriptionsControllerSubpageConfigByShortUuidSignature)
    async def get_subpage_config_by_short_uuid(
        self,
    ) -> saronia.APIResult[
        GetSubpageConfigByShortUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/connection-keys/{uuid}")
    async def get_connection_keys_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetConnectionKeysByUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...


__all__ = ("SubscriptionsController",)
