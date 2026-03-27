import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..remnawave import remnawave
from ..responses import GetSubscriptionRequestHistoryResponseDto, GetSubscriptionRequestHistoryStatsResponseDto

SUBSCRIPTION_REQUEST_HISTORY_CONTROLLER_AUTH = Authorization


@remnawave("/subscription-request-history", auth=SUBSCRIPTION_REQUEST_HISTORY_CONTROLLER_AUTH)
class SubscriptionRequestHistoryController:
    @saronia.get("/", query=True)
    async def get_subscription_request_history(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetSubscriptionRequestHistoryResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.get("/stats")
    async def get_subscription_request_history_stats(
        self,
    ) -> saronia.APIResult[
        GetSubscriptionRequestHistoryStatsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("SubscriptionRequestHistoryController",)
