from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import CreateUserRequestDto, UpdateUserRequestDto
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
        BadRequestError | InternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.post("/", form=CreateUserRequestDto)
    async def create_user(
        self,
    ) -> saronia.APIResult[
        CreateUserResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateUserRequestDto)
    async def update_user(
        self,
    ) -> saronia.APIResult[
        UpdateUserResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_user_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserByUuidResponseDto,
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}/accessible-nodes")
    async def get_user_accessible_nodes(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserAccessibleNodesResponseDto,
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | InternalServerError,
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
        BadRequestError | InternalServerError,
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
        BadRequestError | InternalServerError,
    ]:
        """Args:
        tag: Tag of the user

        """
        ...

    @saronia.post("/{uuid}/actions/revoke", form=PostUsersControllerRevokeUserSubscriptionSignature)
    async def revoke_user_subscription(
        self,
    ) -> saronia.APIResult[
        RevokeUserSubscriptionResponseDto,
        BadRequestError | UserNotFoundError | InternalServerError,
    ]: ...

    @saronia.post("/{uuid}/actions/disable")
    async def disable_user(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DisableUserResponseDto,
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
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
        BadRequestError | UserNotFoundError | InternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...


__all__ = (
    "UserNotFoundError",
    "UsersController",
)
