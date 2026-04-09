import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..remnawave import remnawave
from ..responses import (
    GetLegacyStatsNodesUsersUsageResponseDto,
    GetLegacyStatsUserUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,
)
from ..signatures import (
    GetBandwidthStatsControllerNodesGetStatsNodesUsageSignature,
    GetBandwidthStatsControllerNodeUserUsageSignature,
    GetBandwidthStatsControllerStatsNodeUsersUsageSignature,
    GetBandwidthStatsControllerUsersGetStatsNodesUsageSignature,
    GetBandwidthStatsControllerUserUsageByRangeSignature,
)

BANDWIDTH_STATS_CONTROLLER_AUTH = Authorization


class GetUserUsageByRangeNotFoundError(saronia.StatusError[404]):
    """User not found"""


@remnawave("/bandwidth-stats", auth=BANDWIDTH_STATS_CONTROLLER_AUTH)
class BandwidthStatsController:
    @saronia.get("/nodes/{uuid}/users/legacy", GetBandwidthStatsControllerNodeUserUsageSignature)
    async def get_node_user_usage(
        self,
    ) -> saronia.APIResult[
        GetLegacyStatsNodesUsersUsageResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/nodes/{uuid}/users", GetBandwidthStatsControllerStatsNodeUsersUsageSignature)
    async def get_stats_node_users_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsNodeUsersUsageResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/users/{uuid}/legacy", GetBandwidthStatsControllerUserUsageByRangeSignature)
    async def get_user_usage_by_range(
        self,
    ) -> saronia.APIResult[
        GetLegacyStatsUserUsageResponseDto,
        BadRequestError | GetUserUsageByRangeNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/users/{uuid}", GetBandwidthStatsControllerUsersGetStatsNodesUsageSignature)
    async def users_get_stats_nodes_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsUserUsageResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/nodes", GetBandwidthStatsControllerNodesGetStatsNodesUsageSignature)
    async def nodes_get_stats_nodes_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsNodesUsageResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "BandwidthStatsController",
    "GetUserUsageByRangeNotFoundError",
)
