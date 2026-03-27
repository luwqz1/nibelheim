from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import DropConnectionsRequestDto
from ..remnawave import remnawave
from ..responses import DropConnectionsResponseDto, FetchIpsResponseDto, FetchIpsResultResponseDto

IP_MANAGEMENT_CONTROLLER_AUTH = Authorization


class FetchUserIpsNotFoundError(saronia.StatusError[404]):
    """User not found"""


class GetFetchIpsResultNotFoundError(saronia.StatusError[404]):
    """Job not found"""


class DropConnectionsNotFoundError(saronia.StatusError[404]):
    """User not found // Connected nodes not found"""


@remnawave("/ip-control", auth=IP_MANAGEMENT_CONTROLLER_AUTH)
class IpControlController:
    @saronia.post("/fetch-ips/{uuid}")
    async def fetch_user_ips(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        FetchIpsResponseDto,
        BadRequestError | FetchUserIpsNotFoundError | InternalServerError,
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
        BadRequestError | GetFetchIpsResultNotFoundError | InternalServerError,
    ]:
        """Args:
        job_id: Job ID

        """
        ...

    @saronia.post("/drop-connections", form=DropConnectionsRequestDto)
    async def drop_connections(
        self,
    ) -> saronia.APIResult[
        DropConnectionsResponseDto,
        BadRequestError | DropConnectionsNotFoundError | InternalServerError,
    ]: ...


__all__ = (
    "DropConnectionsNotFoundError",
    "FetchUserIpsNotFoundError",
    "GetFetchIpsResultNotFoundError",
    "IpControlController",
)
