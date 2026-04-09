from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CloneNodePluginRequestDto, CreateNodePluginRequestDto, PluginExecutorRequestDto, ReorderNodePluginsRequestDto, UpdateNodePluginRequestDto
from ..remnawave import remnawave
from ..responses import (
    CloneNodePluginResponseDto,
    CreateNodePluginResponseDto,
    DeleteNodePluginResponseDto,
    GetNodePluginResponseDto,
    GetNodePluginsResponseDto,
    GetTorrentBlockerReportsResponseDto,
    GetTorrentBlockerReportsStatsResponseDto,
    PluginExecutorResponseDto,
    ReorderNodePluginsResponseDto,
    TruncateTorrentBlockerReportsResponseDto,
    UpdateNodePluginResponseDto,
)

NODE_PLUGINS_CONTROLLER_AUTH = Authorization


@remnawave("/node-plugins", auth=NODE_PLUGINS_CONTROLLER_AUTH)
class NodePluginsController:
    @saronia.get("/torrent-blocker", query=True)
    async def get_torrent_blocker_reports(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetTorrentBlockerReportsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.get("/torrent-blocker/stats")
    async def get_torrent_blocker_reports_stats(
        self,
    ) -> saronia.APIResult[
        GetTorrentBlockerReportsStatsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/torrent-blocker/truncate")
    async def truncate_torrent_blocker_reports(
        self,
    ) -> saronia.APIResult[
        TruncateTorrentBlockerReportsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_all_configs(
        self,
    ) -> saronia.APIResult[
        GetNodePluginsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateNodePluginRequestDto)
    async def create_config(
        self,
    ) -> saronia.APIResult[
        CreateNodePluginResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateNodePluginRequestDto)
    async def update_config(
        self,
    ) -> saronia.APIResult[
        UpdateNodePluginResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_config_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetNodePluginResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: Node plugin UUID

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_config(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteNodePluginResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: Node plugin UUID

        """
        ...

    @saronia.post("/actions/reorder", ReorderNodePluginsRequestDto)
    async def reorder_node_plugins(
        self,
    ) -> saronia.APIResult[
        ReorderNodePluginsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/actions/clone", CloneNodePluginRequestDto)
    async def clone_node_plugin(
        self,
    ) -> saronia.APIResult[
        CloneNodePluginResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/executor", PluginExecutorRequestDto)
    async def plugin_executor(
        self,
    ) -> saronia.APIResult[
        PluginExecutorResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("NodePluginsController",)
