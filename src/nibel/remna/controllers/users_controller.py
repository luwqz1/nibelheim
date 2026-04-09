from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CreateUserRequestDto, ResolveUserRequestBodyDto, UpdateUserRequestDto
from ..remnawave import remnawave
from ..responses import (
    CreateUserResponseDto,
    DeleteUserResponseDto,
    DisableUserResponseDto,
    EnableUserResponseDto,
    GetAllTagsResponseDto,
    GetAllUsersResponseDto,
    GetUserAccessibleNodesResponseDto,
    GetUserByEmailResponseDto,
    GetUserByIdResponseDto,
    GetUserByShortUuidResponseDto,
    GetUserByTagResponseDto,
    GetUserByTelegramIdResponseDto,
    GetUserByUsernameResponseDto,
    GetUserByUuidResponseDto,
    GetUserSubscriptionRequestHistoryResponseDto,
    ResetUserTrafficResponseDto,
    ResolveUserResponseDto,
    RevokeUserSubscriptionResponseDto,
    UpdateUserResponseDto,
)
from ..signatures import PostUsersControllerRevokeUserSubscriptionSignature

USERS_CONTROLLER_AUTH = Authorization


class UserNotFoundError(saronia.StatusError[404]):
    """User not found"""


@remnawave("/users", auth=USERS_CONTROLLER_AUTH)
class UsersController:
    @saronia.get("/", query=True)
    async def get_all_users(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetAllUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.post("/", CreateUserRequestDto)
    async def create_user(
        self,
    ) -> saronia.APIResult[
        CreateUserResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateUserRequestDto)
    async def update_user(
        self,
    ) -> saronia.APIResult[
        UpdateUserResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_user_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserByUuidResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_user(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteUserResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.get("/tags")
    async def get_all_tags(
        self,
    ) -> saronia.APIResult[
        GetAllTagsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}/accessible-nodes")
    async def get_user_accessible_nodes(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserAccessibleNodesResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.get("/{uuid}/subscription-request-history")
    async def get_user_subscription_request_history(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserSubscriptionRequestHistoryResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.get("/by-short-uuid/{shortUuid}")
    async def get_user_by_short_uuid(
        self,
        *,
        short_uuid: saronia.Param[str, saronia.Path, "shortUuid"],
    ) -> saronia.APIResult[
        GetUserByShortUuidResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        short_uuid: Short UUID of the user

        """
        ...

    @saronia.get("/by-username/{username}")
    async def get_user_by_username(
        self,
        *,
        username: str,
    ) -> saronia.APIResult[
        GetUserByUsernameResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        username: Username of the user

        """
        ...

    @saronia.get("/by-id/{id}")
    async def get_user_by_id(
        self,
        *,
        id: str,
    ) -> saronia.APIResult[
        GetUserByIdResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        id: ID of the user

        """
        ...

    @saronia.get("/by-telegram-id/{telegramId}")
    async def get_user_by_telegram_id(
        self,
        *,
        telegram_id: saronia.Param[str, saronia.Path, "telegramId"],
    ) -> saronia.APIResult[
        GetUserByTelegramIdResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        telegram_id: Telegram ID of the user

        """
        ...

    @saronia.get("/by-email/{email}")
    async def get_users_by_email(
        self,
        *,
        email: str,
    ) -> saronia.APIResult[
        GetUserByEmailResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        email: Email of the user

        """
        ...

    @saronia.get("/by-tag/{tag}")
    async def get_users_by_tag(
        self,
        *,
        tag: str,
    ) -> saronia.APIResult[
        GetUserByTagResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        tag: Tag of the user

        """
        ...

    @saronia.post("/{uuid}/actions/revoke", PostUsersControllerRevokeUserSubscriptionSignature)
    async def revoke_user_subscription(
        self,
    ) -> saronia.APIResult[
        RevokeUserSubscriptionResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/{uuid}/actions/disable")
    async def disable_user(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DisableUserResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.post("/{uuid}/actions/enable")
    async def enable_user(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        EnableUserResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.post("/{uuid}/actions/reset-traffic")
    async def reset_user_traffic(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        ResetUserTrafficResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.post("/resolve", ResolveUserRequestBodyDto)
    async def resolve_user(
        self,
    ) -> saronia.APIResult[
        ResolveUserResponseDto,
        BadRequestError | UserNotFoundError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "UserNotFoundError",
    "UsersController",
)
