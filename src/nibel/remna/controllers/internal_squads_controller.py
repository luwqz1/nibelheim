from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import CreateInternalSquadRequestDto, ReorderInternalSquadsRequestDto, UpdateInternalSquadRequestDto
from ..remnawave import remnawave
from ..responses import (
    AddUsersToInternalSquadResponseDto,
    CreateInternalSquadResponseDto,
    DeleteInternalSquadResponseDto,
    GetInternalSquadAccessibleNodesResponseDto,
    GetInternalSquadByUuidResponseDto,
    GetInternalSquadsResponseDto,
    RemoveUsersFromInternalSquadResponseDto,
    ReorderInternalSquadsResponseDto,
    UpdateInternalSquadResponseDto,
)

INTERNAL_SQUADS_CONTROLLER_AUTH = Authorization


class InternalSquadConflictError(saronia.StatusError[409]):
    """Internal squad already exists"""


class InternalSquadNotFoundError(saronia.StatusError[404]):
    """Internal squad not found"""


@remnawave("/internal-squads", auth=INTERNAL_SQUADS_CONTROLLER_AUTH)
class InternalSquadsController:
    @saronia.get("/")
    async def get_internal_squads(
        self,
    ) -> saronia.APIResult[
        GetInternalSquadsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateInternalSquadRequestDto)
    async def create_internal_squad(
        self,
    ) -> saronia.APIResult[
        CreateInternalSquadResponseDto,
        BadRequestError | InternalSquadConflictError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateInternalSquadRequestDto)
    async def update_internal_squad(
        self,
    ) -> saronia.APIResult[
        UpdateInternalSquadResponseDto,
        BadRequestError | InternalSquadNotFoundError | InternalSquadConflictError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_internal_squad_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetInternalSquadByUuidResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.delete("/{uuid}")
    async def delete_internal_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteInternalSquadResponseDto,
        BadRequestError | InternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}/accessible-nodes")
    async def get_internal_squad_accessible_nodes(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetInternalSquadAccessibleNodesResponseDto,
        BadRequestError | InternalSquadNotFoundError | InternalServerError,
    ]:
        """Args:
        uuid: UUID of the internal squad

        """
        ...

    @saronia.post("/{uuid}/bulk-actions/add-users")
    async def add_users_to_internal_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        AddUsersToInternalSquadResponseDto,
        BadRequestError | InternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.delete("/{uuid}/bulk-actions/remove-users")
    async def remove_users_from_internal_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        RemoveUsersFromInternalSquadResponseDto,
        BadRequestError | InternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.post("/actions/reorder", form=ReorderInternalSquadsRequestDto)
    async def reorder_internal_squads(
        self,
    ) -> saronia.APIResult[
        ReorderInternalSquadsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = (
    "InternalSquadConflictError",
    "InternalSquadNotFoundError",
    "InternalSquadsController",
)
