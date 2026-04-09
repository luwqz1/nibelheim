from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import (
    CreateInfraBillingHistoryRecordRequestDto,
    CreateInfraBillingNodeRequestDto,
    CreateInfraProviderRequestDto,
    UpdateInfraBillingNodeRequestDto,
    UpdateInfraProviderRequestDto,
)
from ..remnawave import remnawave
from ..responses import (
    CreateInfraBillingHistoryRecordResponseDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderResponseDto,
    DeleteInfraBillingHistoryRecordByUuidResponseDto,
    DeleteInfraBillingNodeByUuidResponseDto,
    DeleteInfraProviderByUuidResponseDto,
    GetInfraBillingHistoryRecordsResponseDto,
    GetInfraBillingNodesResponseDto,
    GetInfraProviderByUuidResponseDto,
    GetInfraProvidersResponseDto,
    UpdateInfraBillingNodeResponseDto,
    UpdateInfraProviderResponseDto,
)

INFRA_BILLING_CONTROLLER_AUTH = Authorization


class GetInfraProviderByUuidNotFoundError(saronia.StatusError[404]):
    """Infra provider not found"""


@remnawave("/infra-billing", auth=INFRA_BILLING_CONTROLLER_AUTH)
class InfraBillingController:
    @saronia.get("/providers")
    async def get_infra_providers(
        self,
    ) -> saronia.APIResult[
        GetInfraProvidersResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/providers", CreateInfraProviderRequestDto)
    async def create_infra_provider(
        self,
    ) -> saronia.APIResult[
        CreateInfraProviderResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/providers", UpdateInfraProviderRequestDto)
    async def update_infra_provider(
        self,
    ) -> saronia.APIResult[
        UpdateInfraProviderResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/providers/{uuid}")
    async def get_infra_provider_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetInfraProviderByUuidResponseDto,
        BadRequestError | GetInfraProviderByUuidNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/providers/{uuid}")
    async def delete_infra_provider_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteInfraProviderByUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/history")
    async def get_infra_billing_history_records(
        self,
    ) -> saronia.APIResult[
        GetInfraBillingHistoryRecordsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/history", CreateInfraBillingHistoryRecordRequestDto)
    async def create_infra_billing_history_record(
        self,
    ) -> saronia.APIResult[
        CreateInfraBillingHistoryRecordResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/history/{uuid}")
    async def delete_infra_billing_history_record_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteInfraBillingHistoryRecordByUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/nodes")
    async def get_billing_nodes(
        self,
    ) -> saronia.APIResult[
        GetInfraBillingNodesResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/nodes", CreateInfraBillingNodeRequestDto)
    async def create_infra_billing_node(
        self,
    ) -> saronia.APIResult[
        CreateInfraBillingNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/nodes", UpdateInfraBillingNodeRequestDto)
    async def update_infra_billing_node(
        self,
    ) -> saronia.APIResult[
        UpdateInfraBillingNodeResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/nodes/{uuid}")
    async def delete_infra_billing_node_by_uuid(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteInfraBillingNodeByUuidResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "GetInfraProviderByUuidNotFoundError",
    "InfraBillingController",
)
