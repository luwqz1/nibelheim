import typing

import msgspec

from typegen.schema.properties import PropertySchema
from typegen.schema.security import Security

type Paths = dict[str, PathMethods]


class SecuritySchema(msgspec.Struct):
    authorization: list[Security] = msgspec.field(default_factory=list, name="Authorization")


class Schema(msgspec.Struct):
    ref: str | None = msgspec.field(default=None, name="$ref")
    type: str | None = msgspec.field(default=None)
    properties: dict[str, PropertySchema] | None = msgspec.field(default=None)


class ApplicationJSON(msgspec.Struct):
    schema: Schema


class RequestBodyContent(msgspec.Struct):
    application_json: ApplicationJSON = msgspec.field(name="application/json")


class RequestBodyResponse(msgspec.Struct):
    description: str
    content: RequestBodyContent | None = msgspec.field(default=None)


class RequestBody(msgspec.Struct):
    required: bool
    content: RequestBodyContent
    responses: dict[str, RequestBodyResponse] | None = msgspec.field(default=None)


class Parameter(msgspec.Struct):
    name: str
    required: bool
    in_: typing.Literal["query", "path"] = msgspec.field(name="in")
    schema: PropertySchema | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)


class PathRequestMethod(msgspec.Struct, kw_only=True):
    operation_id: str = msgspec.field(name="operationId")
    parameters: list[Parameter] = msgspec.field(default_factory=list)
    request_body: RequestBody | None = msgspec.field(default=None, name="requestBody")
    security: list[SecuritySchema] = msgspec.field(default_factory=list)
    summary: str | None = msgspec.field(default=None)
    tags: list[str] = msgspec.field(default_factory=list)


class PathMethods(msgspec.Struct):
    get: PathRequestMethod | None = msgspec.field(default=None)
    post: PathRequestMethod | None = msgspec.field(default=None)
    delete: PathRequestMethod | None = msgspec.field(default=None)
    put: PathRequestMethod | None = msgspec.field(default=None)
    patch: PathRequestMethod | None = msgspec.field(default=None)


__all__ = ("Paths",)
