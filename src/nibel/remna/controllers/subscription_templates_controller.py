from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import CreateSubscriptionTemplateRequestDto, ReorderSubscriptionTemplatesRequestDto, UpdateTemplateRequestDto
from ..remnawave import remnawave
from ..responses import (
    CreateSubscriptionTemplateResponseDto,
    DeleteSubscriptionTemplateResponseDto,
    GetTemplateResponseDto,
    GetTemplatesResponseDto,
    ReorderSubscriptionTemplatesResponseDto,
    UpdateTemplateResponseDto,
)

SUBSCRIPTION_TEMPLATE_CONTROLLER_AUTH = Authorization


@remnawave("/subscription-templates", auth=SUBSCRIPTION_TEMPLATE_CONTROLLER_AUTH)
class SubscriptionTemplatesController:
    @saronia.get("/")
    async def get_all_templates(
        self,
    ) -> saronia.APIResult[
        GetTemplatesResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateSubscriptionTemplateRequestDto)
    async def create_template(
        self,
    ) -> saronia.APIResult[
        CreateSubscriptionTemplateResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateTemplateRequestDto)
    async def update_template(
        self,
    ) -> saronia.APIResult[
        UpdateTemplateResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_template_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetTemplateResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Template UUID

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_template(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteSubscriptionTemplateResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Template UUID

        """
        ...

    @saronia.post("/actions/reorder", form=ReorderSubscriptionTemplatesRequestDto)
    async def reorder_subscription_templates(
        self,
    ) -> saronia.APIResult[
        ReorderSubscriptionTemplatesResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("SubscriptionTemplatesController",)
