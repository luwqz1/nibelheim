from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
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
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateSubscriptionPageConfigRequestDto)
    async def create_config(
        self,
    ) -> saronia.APIResult[
        CreateSubscriptionPageConfigResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateSubscriptionPageConfigRequestDto)
    async def update_config(
        self,
    ) -> saronia.APIResult[
        UpdateSubscriptionPageConfigResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_config_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetSubscriptionPageConfigResponseDto,
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: Subscription page config UUID

        """
        ...

    @saronia.post("/actions/reorder", ReorderSubscriptionPageConfigsRequestDto)
    async def reorder_subscription_page_configs(
        self,
    ) -> saronia.APIResult[
        ReorderSubscriptionPageConfigsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/actions/clone", CloneSubscriptionPageConfigRequestDto)
    async def clone_subscription_page_config(
        self,
    ) -> saronia.APIResult[
        CloneSubscriptionPageConfigResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("SubscriptionPageConfigsController",)
