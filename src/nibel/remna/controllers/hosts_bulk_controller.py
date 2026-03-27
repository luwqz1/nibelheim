import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
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
    @saronia.post("/delete", form=BulkDeleteHostsRequestDto)
    async def delete_hosts(
        self,
    ) -> saronia.APIResult[
        BulkDeleteHostsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/disable", form=BulkDisableHostsRequestDto)
    async def disable_hosts(
        self,
    ) -> saronia.APIResult[
        BulkDisableHostsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/enable", form=BulkEnableHostsRequestDto)
    async def enable_hosts(
        self,
    ) -> saronia.APIResult[
        BulkEnableHostsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/set-inbound", form=SetInboundToManyHostsRequestDto)
    async def set_inbound_to_hosts(
        self,
    ) -> saronia.APIResult[
        SetInboundToManyHostsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/set-port", form=SetPortToManyHostsRequestDto)
    async def set_port_to_hosts(
        self,
    ) -> saronia.APIResult[
        SetPortToManyHostsResponseDto,
        BadRequestError | InternalServerError,
    ]: ...


__all__ = ("HostsBulkController",)
