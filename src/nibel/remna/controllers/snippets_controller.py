import saronia

from ..auth import Authorization
from ..errors import BadRequestError, NotFoundInternalServerError
from ..objects import CreateSnippetRequestDto, DeleteSnippetRequestDto, UpdateSnippetRequestDto
from ..remnawave import remnawave
from ..responses import CreateSnippetResponseDto, DeleteSnippetResponseDto, GetSnippetsResponseDto, UpdateSnippetResponseDto

SNIPPETS_CONTROLLER_AUTH = Authorization


class SnippetConflictError(saronia.StatusError[409]):
    """Snippet name already exists."""


class SnippetNotFoundError(saronia.StatusError[404]):
    """Snippet not found"""


@remnawave("/snippets", auth=SNIPPETS_CONTROLLER_AUTH)
class SnippetsController:
    @saronia.get("/")
    async def get_snippets(
        self,
    ) -> saronia.APIResult[
        GetSnippetsResponseDto,
        BadRequestError | NotFoundInternalServerError,
    ]: ...

    @saronia.post("/", CreateSnippetRequestDto)
    async def create_snippet(
        self,
    ) -> saronia.APIResult[
        CreateSnippetResponseDto,
        BadRequestError | SnippetConflictError | NotFoundInternalServerError,
    ]: ...

    @saronia.delete("/", DeleteSnippetRequestDto)
    async def delete_snippet_by_name(
        self,
    ) -> saronia.APIResult[
        DeleteSnippetResponseDto,
        BadRequestError | SnippetNotFoundError | NotFoundInternalServerError,
    ]: ...

    @saronia.patch("/", UpdateSnippetRequestDto)
    async def update_snippet(
        self,
    ) -> saronia.APIResult[
        UpdateSnippetResponseDto,
        BadRequestError | SnippetNotFoundError | SnippetConflictError | NotFoundInternalServerError,
    ]: ...


__all__ = (
    "SnippetConflictError",
    "SnippetNotFoundError",
    "SnippetsController",
)
