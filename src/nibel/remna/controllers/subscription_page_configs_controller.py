from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import (
    CloneSubscriptionPageConfigRequestDto,
    CreateSubscriptionPageConfigRequestDto,
    ReorderSubscriptionPageConfigsRequestDto,
    UpdateSubscriptionPageConfigRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    CloneSubscriptionPageConfigResponseDto,
    CreateSubscriptionPageConfigResponseDto,
    DeleteSubscriptionPageConfigResponseDto,
    GetSubscriptionPageConfigResponseDto,
    GetSubscriptionPageConfigsResponseDto,
    ReorderSubscriptionPageConfigsResponseDto,
    UpdateSubscriptionPageConfigResponseDto,
)

SUBSCRIPTION_PAGE_CONFIGS_CONTROLLER_AUTH = Authorization


@remnawave("/subscription-page-configs", auth=SUBSCRIPTION_PAGE_CONFIGS_CONTROLLER_AUTH)
class SubscriptionPageConfigsController:
    @saronia.get("/")
    async def get_all_configs(
        self,
    ) -> saronia.APIResult[
        GetSubscriptionPageConfigsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateSubscriptionPageConfigRequestDto)
    async def create_config(
        self,
    ) -> saronia.APIResult[
        CreateSubscriptionPageConfigResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateSubscriptionPageConfigRequestDto)
    async def update_config(
        self,
    ) -> saronia.APIResult[
        UpdateSubscriptionPageConfigResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_config_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetSubscriptionPageConfigResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Subscription page config UUID

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_config(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteSubscriptionPageConfigResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Subscription page config UUID

        """
        ...

    @saronia.post("/actions/reorder", form=ReorderSubscriptionPageConfigsRequestDto)
    async def reorder_subscription_page_configs(
        self,
    ) -> saronia.APIResult[
        ReorderSubscriptionPageConfigsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/actions/clone", form=CloneSubscriptionPageConfigRequestDto)
    async def clone_subscription_page_config(
        self,
    ) -> saronia.APIResult[
        CloneSubscriptionPageConfigResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("SubscriptionPageConfigsController",)
