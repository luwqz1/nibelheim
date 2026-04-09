from uuid import UUID

import kungfu
import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..remnawave import remnawave
from ..responses import GetNodeMetadataResponseDto, GetUserMetadataResponseDto, UpsertNodeMetadataResponseDto, UpsertUserMetadataResponseDto
from ..signatures import PutMetadataControllerUpsertNodeMetadataSignature, PutMetadataControllerUpsertUserMetadataSignature

METADATA_CONTROLLER_AUTH = Authorization


@remnawave("/metadata", auth=METADATA_CONTROLLER_AUTH)
class MetadataController:
    @saronia.get("/user/{uuid}")
    async def get_user_metadata(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetUserMetadataResponseDto,
        BadRequestError | kungfu.Sum[NotFoundInternalServerError, NotFoundInternalServerError] | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the user

        """
        ...

    @saronia.put("/user/{uuid}", PutMetadataControllerUpsertUserMetadataSignature)
    async def upsert_user_metadata(
        self,
    ) -> saronia.APIResult[
        UpsertUserMetadataResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.get("/node/{uuid}")
    async def get_node_metadata(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        GetNodeMetadataResponseDto,
        BadRequestError | kungfu.Sum[NotFoundInternalServerError, NotFoundInternalServerError] | NotFoundInternalServerError,
    ]:
        """Args:
        uuid: UUID of the node

        """
        ...

    @saronia.put("/node/{uuid}", PutMetadataControllerUpsertNodeMetadataSignature)
    async def upsert_node_metadata(
        self,
    ) -> saronia.APIResult[
        UpsertNodeMetadataResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("MetadataController",)
