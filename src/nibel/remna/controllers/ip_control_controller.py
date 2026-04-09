from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import DropConnectionsRequestDto
from ..remnawave import remnawave
from ..responses import DropConnectionsResponseDto, FetchIpsResponseDto, FetchIpsResultResponseDto, FetchUsersIpsResponseDto, FetchUsersIpsResultResponseDto

IP_MANAGEMENT_CONTROLLER_AUTH = Authorization


class FetchUserIpsNotFoundError(saronia.StatusError[404]):
    """User not found"""


class IpControlNotFoundError(saronia.StatusError[404]):
    """Job not found"""


class DropConnectionsNotFoundError(saronia.StatusError[404]):
    """User not found // Connected nodes not found"""


class FetchUsersIpsNotFoundError(saronia.StatusError[404]):
    """Node not found"""


@remnawave("/ip-control", auth=IP_MANAGEMENT_CONTROLLER_AUTH)
class IpControlController:
    @saronia.post("/fetch-ips/{uuid}")
    async def fetch_user_ips(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        FetchIpsResponseDto,
        BadRequestError | FetchUserIpsNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.get("/fetch-ips/result/{jobId}")
    async def get_fetch_ips_result(
        self,
        *,
        job_id: saronia.Param[str, saronia.Path, "jobId"],
    ) -> saronia.APIResult[
        FetchIpsResultResponseDto,
        BadRequestError | IpControlNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        job_id: Job ID

        """
        ...

    @saronia.post("/drop-connections", DropConnectionsRequestDto)
    async def drop_connections(
        self,
    ) -> saronia.APIResult[
        DropConnectionsResponseDto,
        BadRequestError | DropConnectionsNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/fetch-users-ips/{nodeUuid}")
    async def fetch_users_ips(
        self,
        *,
        node_uuid: saronia.Param[str, saronia.Path, "nodeUuid"],
    ) -> saronia.APIResult[
        FetchUsersIpsResponseDto,
        BadRequestError | FetchUsersIpsNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        node_uuid: UUID of the node

        """
        ...

    @saronia.get("/fetch-users-ips/result/{jobId}")
    async def get_fetch_users_ips_result(
        self,
        *,
        job_id: saronia.Param[str, saronia.Path, "jobId"],
    ) -> saronia.APIResult[
        FetchUsersIpsResultResponseDto,
        BadRequestError | IpControlNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        job_id: Job ID

        """
        ...


__all__ = (
    "DropConnectionsNotFoundError",
    "FetchUserIpsNotFoundError",
    "FetchUsersIpsNotFoundError",
    "IpControlController",
    "IpControlNotFoundError",
)
