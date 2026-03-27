from uuid import UUID

import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
from ..objects import CreateApiTokenRequestDto
from ..remnawave import remnawave
from ..responses import CreateApiTokenResponseDto, DeleteApiTokenResponseDto, FindAllApiTokensResponseDto

API_TOKENS_CONTROLLER_AUTH = Authorization


@remnawave("/tokens", auth=API_TOKENS_CONTROLLER_AUTH)
class TokensController:
    @saronia.get("/")
    async def find_all(
        self,
    ) -> saronia.APIResult[
        FindAllApiTokensResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """This endpoint is forbidden to use via "API-key". It can only be used with admin JWT-token."""
        ...

    @saronia.post("/", form=CreateApiTokenRequestDto)
    async def create(
        self,
    ) -> saronia.APIResult[
        CreateApiTokenResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """This endpoint is forbidden to use via "API-key". It can only be used with an admin JWT-token."""
        ...

    @saronia.delete("/{uuid}")
    async def delete(
        self,
        *,
        uuid: UUID,
    ) -> saronia.APIResult[
        DeleteApiTokenResponseDto,
        BadRequestError | InternalServerError,
    ]:
        """This endpoint is forbidden to use via "API-key". It can be used only with an admin JWT-token.

        Args:
            uuid: UUID of the API token

        """
        ...


__all__ = ("TokensController",)
