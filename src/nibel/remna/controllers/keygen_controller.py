import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..remnawave import remnawave
from ..responses import GetPubKeyResponseDto

KEYGEN_CONTROLLER_AUTH = Authorization


@remnawave("/keygen", auth=KEYGEN_CONTROLLER_AUTH)
class KeygenController:
    @saronia.get("/")
    async def generate_key(
        self,
    ) -> saronia.APIResult[
        GetPubKeyResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...


__all__ = ("KeygenController",)
