from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import CreateExternalSquadRequestDto, ReorderExternalSquadsRequestDto, UpdateExternalSquadRequestDto
from ..remnawave import remnawave
from ..responses import (
    AddUsersToExternalSquadResponseDto,
    CreateExternalSquadResponseDto,
    DeleteExternalSquadResponseDto,
    GetExternalSquadByUuidResponseDto,
    GetExternalSquadsResponseDto,
    RemoveUsersFromExternalSquadResponseDto,
    ReorderExternalSquadsResponseDto,
    UpdateExternalSquadResponseDto,
)

EXTERNAL_SQUADS_CONTROLLER_AUTH = Authorization


class ExternalSquadConflictError(saronia.StatusError[409]):
    """External squad already exists"""


class ExternalSquadNotFoundError(saronia.StatusError[404]):
    """External squad not found"""


@remnawave("/external-squads", auth=EXTERNAL_SQUADS_CONTROLLER_AUTH)
class ExternalSquadsController:
    @saronia.get("/")
    async def get_external_squads(
        self,
    ) -> saronia.APIResult[
        GetExternalSquadsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateExternalSquadRequestDto)
    async def create_external_squad(
        self,
    ) -> saronia.APIResult[
        CreateExternalSquadResponseDto,
        BadRequestError | ExternalSquadConflictError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateExternalSquadRequestDto)
    async def update_external_squad(
        self,
    ) -> saronia.APIResult[
        UpdateExternalSquadResponseDto,
        BadRequestError | ExternalSquadNotFoundError | ExternalSquadConflictError | InternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_external_squad_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetExternalSquadByUuidResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.delete("/{uuid}")
    async def delete_external_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteExternalSquadResponseDto,
        BadRequestError | ExternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.post("/{uuid}/bulk-actions/add-users")
    async def add_users_to_external_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        AddUsersToExternalSquadResponseDto,
        BadRequestError | ExternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.delete("/{uuid}/bulk-actions/remove-users")
    async def remove_users_from_external_squad(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        RemoveUsersFromExternalSquadResponseDto,
        BadRequestError | ExternalSquadNotFoundError | InternalServerError,
    ]: ...

    @saronia.post("/actions/reorder", form=ReorderExternalSquadsRequestDto)
    async def reorder_external_squads(
        self,
    ) -> saronia.APIResult[
        ReorderExternalSquadsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = (
    "ExternalSquadConflictError",
    "ExternalSquadNotFoundError",
    "ExternalSquadsController",
)
