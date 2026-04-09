from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CreateConfigProfileRequestDto, ReorderConfigProfilesRequestDto, UpdateConfigProfileRequestDto
from ..remnawave import remnawave
from ..responses import (
    CreateConfigProfileResponseDto,
    DeleteConfigProfileResponseDto,
    GetAllInboundsResponseDto,
    GetComputedConfigProfileByUuidResponseDto,
    GetConfigProfileByUuidResponseDto,
    GetConfigProfilesResponseDto,
    GetInboundsByProfileUuidResponseDto,
    ReorderConfigProfilesResponseDto,
    UpdateConfigProfileResponseDto,
)

CONFIG_PROFILES_CONTROLLER_AUTH = Authorization


class ConfigProfileConflictError(saronia.StatusError[409]):
    """Config profile name already exists or inbound tags are not unique. Inbound tags must be unique in global scope."""


class ConfigProfileNotFoundError(saronia.StatusError[404]):
    """Config profile not found"""


@remnawave("/config-profiles", auth=CONFIG_PROFILES_CONTROLLER_AUTH)
class ConfigProfilesController:
    @saronia.get("/")
    async def get_config_profiles(
        self,
    ) -> saronia.APIResult[
        GetConfigProfilesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateConfigProfileRequestDto)
    async def create_config_profile(
        self,
    ) -> saronia.APIResult[
        CreateConfigProfileResponseDto,
        BadRequestError | ConfigProfileConflictError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateConfigProfileRequestDto)
    async def update_config_profile(
        self,
    ) -> saronia.APIResult[
        UpdateConfigProfileResponseDto,
        BadRequestError | ConfigProfileNotFoundError | ConfigProfileConflictError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/inbounds")
    async def get_all_inbounds(
        self,
    ) -> saronia.APIResult[
        GetAllInboundsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}/inbounds")
    async def get_inbounds_by_profile_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetInboundsByProfileUuidResponseDto,
        BadRequestError | ConfigProfileNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}")
    async def get_config_profile_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetConfigProfileByUuidResponseDto,
        BadRequestError | ConfigProfileNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/{uuid}")
    async def delete_config_profile_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteConfigProfileResponseDto,
        BadRequestError | ConfigProfileNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/{uuid}/computed-config")
    async def get_computed_config_profile_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetComputedConfigProfileByUuidResponseDto,
        BadRequestError | ConfigProfileNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/actions/reorder", ReorderConfigProfilesRequestDto)
    async def reorder_config_profiles(
        self,
    ) -> saronia.APIResult[
        ReorderConfigProfilesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "ConfigProfileConflictError",
    "ConfigProfileNotFoundError",
    "ConfigProfilesController",
)
