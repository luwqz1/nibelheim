import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import DebugSrrMatcherRequestDto, EncryptHappCryptoLinkRequestDto
from ..remnawave import remnawave
from ..responses import (
    DebugSrrMatcherResponseDto,
    EncryptHappCryptoLinkResponseDto,
    GenerateX25519ResponseDto,
    GetBandwidthStatsResponseDto,
    GetMetadataResponseDto,
    GetNodesMetricsResponseDto,
    GetNodesStatisticsResponseDto,
    GetRemnawaveHealthResponseDto,
    GetStatsResponseDto,
)

SYSTEM_CONTROLLER_AUTH = Authorization


@remnawave("/system", auth=SYSTEM_CONTROLLER_AUTH)
class SystemController:
    @saronia.get("/metadata")
    async def get_metadata(
        self,
    ) -> saronia.APIResult[
        GetMetadataResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/stats")
    async def get_stats(
        self,
    ) -> saronia.APIResult[
        GetStatsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/stats/bandwidth")
    async def get_bandwidth_stats(
        self,
    ) -> saronia.APIResult[
        GetBandwidthStatsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/stats/nodes")
    async def get_nodes_statistics(
        self,
    ) -> saronia.APIResult[
        GetNodesStatisticsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/health")
    async def get_remnawave_health(
        self,
    ) -> saronia.APIResult[
        GetRemnawaveHealthResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/nodes/metrics")
    async def get_nodes_metrics(
        self,
    ) -> saronia.APIResult[
        GetNodesMetricsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/tools/x25519/generate")
    async def get_x25519_keypairs(
        self,
    ) -> saronia.APIResult[
        GenerateX25519ResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/tools/happ/encrypt", form=EncryptHappCryptoLinkRequestDto)
    async def encrypt_happ_crypto_link(
        self,
    ) -> saronia.APIResult[
        EncryptHappCryptoLinkResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/testers/srr-matcher", form=DebugSrrMatcherRequestDto)
    async def debug_srr_matcher(
        self,
    ) -> saronia.APIResult[
        DebugSrrMatcherResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("SystemController",)
