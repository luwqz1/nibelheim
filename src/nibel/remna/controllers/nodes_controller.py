from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import (
    BulkNodesActionsRequestDto,
    CreateNodeRequestDto,
    ProfileModificationRequestDto,
    ReorderNodeRequestDto,
    RestartAllNodesRequestBodyDto,
    UpdateNodeRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    BulkNodesActionsResponseDto,
    CreateNodeResponseDto,
    DeleteNodeResponseDto,
    DisableNodeResponseDto,
    EnableNodeResponseDto,
    GetAllNodesResponseDto,
    GetAllNodesTagsResponseDto,
    GetOneNodeResponseDto,
    ProfileModificationResponseDto,
    ReorderNodeResponseDto,
    ResetNodeTrafficResponseDto,
    RestartAllNodesResponseDto,
    RestartNodeResponseDto,
    UpdateNodeResponseDto,
)

NODES_CONTROLLER_AUTH = Authorization


@remnawave("/nodes", auth=NODES_CONTROLLER_AUTH)
class NodesController:
    @saronia.get("/tags")
    async def get_all_nodes_tags(
        self,
    ) -> saronia.APIResult[
        GetAllNodesTagsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_all_nodes(
        self,
    ) -> saronia.APIResult[
        GetAllNodesResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateNodeRequestDto)
    async def create_node(
        self,
    ) -> saronia.APIResult[
        CreateNodeResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateNodeRequestDto)
    async def update_node(
        self,
    ) -> saronia.APIResult[
        UpdateNodeResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_one_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetOneNodeResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteNodeResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/{uuid}/actions/enable")
    async def enable_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        EnableNodeResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/{uuid}/actions/disable")
    async def disable_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DisableNodeResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/{uuid}/actions/restart")
    async def restart_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        RestartNodeResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/{uuid}/actions/reset-traffic")
    async def reset_node_traffic(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        ResetNodeTrafficResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/actions/restart-all", form=RestartAllNodesRequestBodyDto)
    async def restart_all_nodes(
        self,
    ) -> saronia.APIResult[
        RestartAllNodesResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/actions/reorder", form=ReorderNodeRequestDto)
    async def reorder_nodes(
        self,
    ) -> saronia.APIResult[
        ReorderNodeResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/bulk-actions/profile-modification", form=ProfileModificationRequestDto)
    async def profile_modification(
        self,
    ) -> saronia.APIResult[
        ProfileModificationResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/bulk-actions", form=BulkNodesActionsRequestDto)
    async def bulk_nodes_actions(
        self,
    ) -> saronia.APIResult[
        BulkNodesActionsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("NodesController",)
