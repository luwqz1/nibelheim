import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import (
    BulkDeleteHostsRequestDto,
    BulkDisableHostsRequestDto,
    BulkEnableHostsRequestDto,
    SetInboundToManyHostsRequestDto,
    SetPortToManyHostsRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    BulkDeleteHostsResponseDto,
    BulkDisableHostsResponseDto,
    BulkEnableHostsResponseDto,
    SetInboundToManyHostsResponseDto,
    SetPortToManyHostsResponseDto,
)

HOSTS_BULK_ACTIONS_CONTROLLER_AUTH = Authorization


@remnawave("/hosts/bulk", auth=HOSTS_BULK_ACTIONS_CONTROLLER_AUTH)
class HostsBulkController:
    @saronia.post("/delete", BulkDeleteHostsRequestDto)
    async def delete_hosts(
        self,
    ) -> saronia.APIResult[
        BulkDeleteHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/disable", BulkDisableHostsRequestDto)
    async def disable_hosts(
        self,
    ) -> saronia.APIResult[
        BulkDisableHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/enable", BulkEnableHostsRequestDto)
    async def enable_hosts(
        self,
    ) -> saronia.APIResult[
        BulkEnableHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/set-inbound", SetInboundToManyHostsRequestDto)
    async def set_inbound_to_hosts(
        self,
    ) -> saronia.APIResult[
        SetInboundToManyHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/set-port", SetPortToManyHostsRequestDto)
    async def set_port_to_hosts(
        self,
    ) -> saronia.APIResult[
        SetPortToManyHostsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("HostsBulkController",)
