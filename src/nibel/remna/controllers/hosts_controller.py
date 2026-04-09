from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CreateHostRequestDto, ReorderHostRequestDto, UpdateHostRequestDto
from ..remnawave import remnawave
from ..responses import (
    CreateHostResponseDto,
    DeleteHostResponseDto,
    GetAllHostsResponseDto,
    GetAllHostTagsResponseDto,
    GetOneHostResponseDto,
    ReorderHostResponseDto,
    UpdateHostResponseDto,
)

HOSTS_CONTROLLER_AUTH = Authorization


class DeleteHostNotFoundError(saronia.StatusError[404]):
    """Host not found"""


@remnawave("/hosts", auth=HOSTS_CONTROLLER_AUTH)
class HostsController:
    @saronia.get("/tags")
    async def get_all_host_tags(
        self,
    ) -> saronia.APIResult[
        GetAllHostTagsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/")
    async def get_all_hosts(
        self,
    ) -> saronia.APIResult[
        GetAllHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateHostRequestDto)
    async def create_host(
        self,
    ) -> saronia.APIResult[
        CreateHostResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateHostRequestDto)
    async def update_host(
        self,
    ) -> saronia.APIResult[
        UpdateHostResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_one_host(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetOneHostResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the host

        """
        ...

    @saronia.delete("/{uuid}")
    async def delete_host(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteHostResponseDto,
        BadRequestError | DeleteHostNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the host

        """
        ...

    @saronia.post("/actions/reorder", ReorderHostRequestDto)
    async def reorder_hosts(
        self,
    ) -> saronia.APIResult[
        ReorderHostResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "DeleteHostNotFoundError",
    "HostsController",
)
