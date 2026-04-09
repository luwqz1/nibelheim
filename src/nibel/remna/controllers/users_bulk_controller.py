import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import (
    BulkAllExtendExpirationDateRequestDto,
    BulkAllUpdateUsersRequestDto,
    BulkDeleteUsersByStatusRequestDto,
    BulkDeleteUsersRequestDto,
    BulkExtendExpirationDateRequestDto,
    BulkResetTrafficUsersRequestDto,
    BulkRevokeUsersSubscriptionRequestDto,
    BulkUpdateUsersRequestDto,
    BulkUpdateUsersSquadsRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    BulkAllExtendExpirationDateResponseDto,
    BulkAllResetTrafficUsersResponseDto,
    BulkAllUpdateUsersResponseDto,
    BulkDeleteUsersByStatusResponseDto,
    BulkDeleteUsersResponseDto,
    BulkExtendExpirationDateResponseDto,
    BulkResetTrafficUsersResponseDto,
    BulkRevokeUsersSubscriptionResponseDto,
    BulkUpdateUsersResponseDto,
    BulkUpdateUsersSquadsResponseDto,
)

USERS_BULK_ACTIONS_CONTROLLER_AUTH = Authorization


@remnawave("/users/bulk", auth=USERS_BULK_ACTIONS_CONTROLLER_AUTH)
class UsersBulkController:
    @saronia.post("/delete-by-status", BulkDeleteUsersByStatusRequestDto)
    async def bulk_delete_users_by_status(
        self,
    ) -> saronia.APIResult[
        BulkDeleteUsersByStatusResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/delete", BulkDeleteUsersRequestDto)
    async def bulk_delete_users(
        self,
    ) -> saronia.APIResult[
        BulkDeleteUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/revoke-subscription", BulkRevokeUsersSubscriptionRequestDto)
    async def bulk_revoke_users_subscription(
        self,
    ) -> saronia.APIResult[
        BulkRevokeUsersSubscriptionResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/reset-traffic", BulkResetTrafficUsersRequestDto)
    async def bulk_reset_user_traffic(
        self,
    ) -> saronia.APIResult[
        BulkResetTrafficUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/update", BulkUpdateUsersRequestDto)
    async def bulk_update_users(
        self,
    ) -> saronia.APIResult[
        BulkUpdateUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/update-squads", BulkUpdateUsersSquadsRequestDto)
    async def bulk_update_users_internal_squads(
        self,
    ) -> saronia.APIResult[
        BulkUpdateUsersSquadsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/extend-expiration-date", BulkExtendExpirationDateRequestDto)
    async def bulk_extend_expiration_date(
        self,
    ) -> saronia.APIResult[
        BulkExtendExpirationDateResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Bulk extend all users expiration date"""
        ...

    @saronia.post("/all/update", BulkAllUpdateUsersRequestDto)
    async def bulk_update_all_users(
        self,
    ) -> saronia.APIResult[
        BulkAllUpdateUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/all/reset-traffic")
    async def bulk_all_reset_user_traffic(
        self,
    ) -> saronia.APIResult[
        BulkAllResetTrafficUsersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Bulk reset all users traffic"""
        ...

    @saronia.post("/all/extend-expiration-date", BulkAllExtendExpirationDateRequestDto)
    async def bulk_all_extend_expiration_date(
        self,
    ) -> saronia.APIResult[
        BulkAllExtendExpirationDateResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Bulk extend all users expiration date"""
        ...


__all__ = ("UsersBulkController",)
