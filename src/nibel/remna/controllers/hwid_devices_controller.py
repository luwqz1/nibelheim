import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CreateUserHwidDeviceRequestDto, DeleteAllUserHwidDevicesRequestDto, DeleteUserHwidDeviceRequestDto
from ..remnawave import remnawave
from ..responses import (
    CreateUserHwidDeviceResponseDto,
    DeleteAllUserHwidDevicesResponseDto,
    DeleteUserHwidDeviceResponseDto,
    GetAllHwidDevicesResponseDto,
    GetHwidDevicesStatsResponseDto,
    GetTopUsersByHwidDevicesResponseDto,
    GetUserHwidDevicesResponseDto,
)

HWID_USER_DEVICES_CONTROLLER_AUTH = Authorization


class HwidDeviceNotFoundError(saronia.StatusError[404]):
    """One of requested resources not found"""


@remnawave("/hwid/devices", auth=HWID_USER_DEVICES_CONTROLLER_AUTH)
class HwidDevicesController:
    @saronia.get("/", query=True)
    async def get_all_users(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetAllHwidDevicesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.post("/", CreateUserHwidDeviceRequestDto)
    async def create_user_hwid_device(
        self,
    ) -> saronia.APIResult[
        CreateUserHwidDeviceResponseDto,
        BadRequestError | HwidDeviceNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/delete", DeleteUserHwidDeviceRequestDto)
    async def delete_user_hwid_device(
        self,
    ) -> saronia.APIResult[
        DeleteUserHwidDeviceResponseDto,
        BadRequestError | HwidDeviceNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/delete-all", DeleteAllUserHwidDevicesRequestDto)
    async def delete_all_user_hwid_devices(
        self,
    ) -> saronia.APIResult[
        DeleteAllUserHwidDevicesResponseDto,
        BadRequestError | HwidDeviceNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/stats")
    async def get_hwid_devices_stats(
        self,
    ) -> saronia.APIResult[
        GetHwidDevicesStatsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/top-users", query=True)
    async def get_top_users_by_hwid_devices(
        self,
        *,
        size: int | None = None,
        start: int | None = None,
    ) -> saronia.APIResult[
        GetTopUsersByHwidDevicesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]:
        """Args:
        size: Page size for pagination
        start: Offset for pagination

        """
        ...

    @saronia.get("/{userUuid}")
    async def get_user_hwid_devices(
        self,
        *,
        user_uuid: saronia.Param[str, saronia.Path, "userUuid"],
    ) -> saronia.APIResult[
        GetUserHwidDevicesResponseDto,
        BadRequestError | HwidDeviceNotFoundError | NotFoundInternalServerError,
    ]:
        """Args:
        user_uuid: UUID of the user

        """
        ...


__all__ = (
    "HwidDeviceNotFoundError",
    "HwidDevicesController",
)
