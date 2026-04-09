from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import (
    BulkNodesActionsRequestDto,
    BulkNodesUpdateRequestDto,
    CreateNodeRequestDto,
    ProfileModificationRequestDto,
    ReorderNodeRequestDto,
    RestartAllNodesRequestBodyDto,
    UpdateNodeRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    BulkNodesActionsResponseDto,
    BulkNodesUpdateResponseDto,
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
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_all_nodes(
        self,
    ) -> saronia.APIResult[
        GetAllNodesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateNodeRequestDto)
    async def create_node(
        self,
    ) -> saronia.APIResult[
        CreateNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateNodeRequestDto)
    async def update_node(
        self,
    ) -> saronia.APIResult[
        UpdateNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_one_node(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetOneNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
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
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: Node UUID

        """
        ...

    @saronia.post("/actions/restart-all", RestartAllNodesRequestBodyDto)
    async def restart_all_nodes(
        self,
    ) -> saronia.APIResult[
        RestartAllNodesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/actions/reorder", ReorderNodeRequestDto)
    async def reorder_nodes(
        self,
    ) -> saronia.APIResult[
        ReorderNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/bulk-actions/profile-modification", ProfileModificationRequestDto)
    async def profile_modification(
        self,
    ) -> saronia.APIResult[
        ProfileModificationResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/bulk-actions", BulkNodesActionsRequestDto)
    async def bulk_nodes_actions(
        self,
    ) -> saronia.APIResult[
        BulkNodesActionsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/bulk-actions/update", BulkNodesUpdateRequestDto)
    async def bulk_nodes_update(
        self,
    ) -> saronia.APIResult[
        BulkNodesUpdateResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("NodesController",)
