import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..remnawave import remnawave
from ..responses import (
    GetLegacyStatsNodesUsersUsageResponseDto,
    GetLegacyStatsUserUsageResponseDto,
    GetStatsNodesRealtimeUsageResponseDto,
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
    @saronia.get("/nodes/{uuid}/users/legacy", form=GetBandwidthStatsControllerNodeUserUsageSignature)
    async def get_node_user_usage(
        self,
    ) -> saronia.APIResult[
        GetLegacyStatsNodesUsersUsageResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/nodes/realtime")
    async def get_nodes_realtime_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsNodesRealtimeUsageResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/nodes/{uuid}/users", form=GetBandwidthStatsControllerStatsNodeUsersUsageSignature)
    async def get_stats_node_users_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsNodeUsersUsageResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/users/{uuid}/legacy", form=GetBandwidthStatsControllerUserUsageByRangeSignature)
    async def get_user_usage_by_range(
        self,
    ) -> saronia.APIResult[
        GetLegacyStatsUserUsageResponseDto,
        BadRequestError | GetUserUsageByRangeNotFoundError | InternalServerError,
    ]: ...

    @saronia.get("/users/{uuid}", form=GetBandwidthStatsControllerUsersGetStatsNodesUsageSignature)
    async def users_get_stats_nodes_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsUserUsageResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/nodes", form=GetBandwidthStatsControllerNodesGetStatsNodesUsageSignature)
    async def nodes_get_stats_nodes_usage(
        self,
    ) -> saronia.APIResult[
        GetStatsNodesUsageResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = (
    "BandwidthStatsController",
    "GetUserUsageByRangeNotFoundError",
)
