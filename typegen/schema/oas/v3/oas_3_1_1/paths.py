import typing

import msgspec

from typegen.model import Model
from typegen.schema.oas.v3.oas_3_1_1.properties import PropertySchema
from typegen.schema.oas.v3.oas_3_1_1.security import Security

type Paths = dict[str, PathMethods]


class SecuritySchema(Model):
    authorization: list[Security] = msgspec.field(default_factory=list, name="Authorization")


class Schema(Model):
    ref: str | None = msgspec.field(default=None, name="$ref")
    type: str | None = msgspec.field(default=None)
    properties: dict[str, PropertySchema] | None = msgspec.field(default=None)


class ApplicationJSON(Model):
    schema: Schema


class RequestBodyContent(Model):
    application_json: ApplicationJSON = msgspec.field(name="application/json")


class RequestBodyResponse(Model):
    description: str
    content: RequestBodyContent | None = msgspec.field(default=None)


class RequestBody(Model):
    required: bool
    content: RequestBodyContent


class Parameter(Model):
    name: str
    required: bool
    in_: typing.Literal["query", "path"] = msgspec.field(name="in")
    schema: PropertySchema | None = msgspec.field(default=None)
    description: str | None = msgspec.field(default=None)


class PathRequestMethod(Model, kw_only=True):
    operation_id: str = msgspec.field(name="operationId")
    parameters: list[Parameter] = msgspec.field(default_factory=list)
    request_body: RequestBody | None = msgspec.field(default=None, name="requestBody")
    security: list[SecuritySchema] = msgspec.field(default_factory=list)
    summary: str | None = msgspec.field(default=None)
    tags: list[str] = msgspec.field(default_factory=list)
    description: str | None = msgspec.field(default=None)
    responses: dict[str, RequestBodyResponse] | None = msgspec.field(default=None)


class PathMethods(Model):
    get: PathRequestMethod | None = msgspec.field(default=None)
    post: PathRequestMethod | None = msgspec.field(default=None)
    delete: PathRequestMethod | None = msgspec.field(default=None)
    put: PathRequestMethod | None = msgspec.field(default=None)
    patch: PathRequestMethod | None = msgspec.field(default=None)


__all__ = ("Paths",)
