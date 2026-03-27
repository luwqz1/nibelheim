import saronia

from ..auth import Authorization
from ..errors import BadRequestError, InternalServerError
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
        BadRequestError | InternalServerError,
    ]: ...

    @saronia.post("/", form=CreateSnippetRequestDto)
    async def create_snippet(
        self,
    ) -> saronia.APIResult[
        CreateSnippetResponseDto,
        BadRequestError | SnippetConflictError | InternalServerError,
    ]: ...

    @saronia.delete("/", form=DeleteSnippetRequestDto)
    async def delete_snippet_by_name(
        self,
    ) -> saronia.APIResult[
        DeleteSnippetResponseDto,
        BadRequestError | SnippetNotFoundError | InternalServerError,
    ]: ...

    @saronia.patch("/", form=UpdateSnippetRequestDto)
    async def update_snippet(
        self,
    ) -> saronia.APIResult[
        UpdateSnippetResponseDto,
        BadRequestError | SnippetNotFoundError | SnippetConflictError | InternalServerError,
    ]: ...


__all__ = (
    "SnippetConflictError",
    "SnippetNotFoundError",
    "SnippetsController",
)
