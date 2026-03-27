import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
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
    @saronia.post("/delete-by-status", form=BulkDeleteUsersByStatusRequestDto)
    async def bulk_delete_users_by_status(
        self,
    ) -> saronia.APIResult[
        BulkDeleteUsersByStatusResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/delete", form=BulkDeleteUsersRequestDto)
    async def bulk_delete_users(
        self,
    ) -> saronia.APIResult[
        BulkDeleteUsersResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/revoke-subscription", form=BulkRevokeUsersSubscriptionRequestDto)
    async def bulk_revoke_users_subscription(
        self,
    ) -> saronia.APIResult[
        BulkRevokeUsersSubscriptionResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/reset-traffic", form=BulkResetTrafficUsersRequestDto)
    async def bulk_reset_user_traffic(
        self,
    ) -> saronia.APIResult[
        BulkResetTrafficUsersResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/update", form=BulkUpdateUsersRequestDto)
    async def bulk_update_users(
        self,
    ) -> saronia.APIResult[
        BulkUpdateUsersResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/update-squads", form=BulkUpdateUsersSquadsRequestDto)
    async def bulk_update_users_internal_squads(
        self,
    ) -> saronia.APIResult[
        BulkUpdateUsersSquadsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/extend-expiration-date", form=BulkExtendExpirationDateRequestDto)
    async def bulk_extend_expiration_date(
        self,
    ) -> saronia.APIResult[
        BulkExtendExpirationDateResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Bulk extend all users expiration date"""
        ...

    @saronia.post("/all/update", form=BulkAllUpdateUsersRequestDto)
    async def bulk_update_all_users(
        self,
    ) -> saronia.APIResult[
        BulkAllUpdateUsersResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/all/reset-traffic")
    async def bulk_all_reset_user_traffic(
        self,
    ) -> saronia.APIResult[
        BulkAllResetTrafficUsersResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Bulk reset all users traffic"""
        ...

    @saronia.post("/all/extend-expiration-date", form=BulkAllExtendExpirationDateRequestDto)
    async def bulk_all_extend_expiration_date(
        self,
    ) -> saronia.APIResult[
        BulkAllExtendExpirationDateResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Bulk extend all users expiration date"""
        ...


__all__ = ("UsersBulkController",)
