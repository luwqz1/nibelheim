from __future__ import annotations

from datetime import datetime
from http import HTTPStatus

import msgspex
import saronia

from .objects import BadRequestErrorErrors


class AuthControllerAuthBase(msgspex.Model, kw_only=True):
    message: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    status_code: msgspex.Option[int] = msgspex.field(default=..., name="statusCode", converter=msgspex.From[int | None])


class InternalServerBase(msgspex.Model, kw_only=True):
    path: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    message: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    error_code: msgspex.Option[str] = msgspex.field(default=..., name="errorCode", converter=msgspex.From[str | None])


class BadRequestError(AuthControllerAuthBase, saronia.ModelStatusError[HTTPStatus.BAD_REQUEST], kw_only=True):
    """Validation error"""

    errors: msgspex.Option[list[BadRequestErrorErrors]] = msgspex.field(default=..., converter=msgspex.From["list[BadRequestErrorErrors] | None"])


class InternalServerError(InternalServerBase, saronia.ModelStatusError[HTTPStatus.INTERNAL_SERVER_ERROR], kw_only=True):
    """Server error"""

    timestamp: msgspex.Option[msgspex.StringTimestampDatetime] = msgspex.field(default=..., converter=msgspex.From[str | datetime | None])


class AuthControllerAuthError(AuthControllerAuthBase, saronia.ModelStatusError[HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN], kw_only=True):
    """Unauthorized - Invalid credentials"""

    error: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])


class SubscriptionsControllerNotFoundError(InternalServerBase, saronia.ModelStatusError[HTTPStatus.NOT_FOUND], kw_only=True):
    """User not found"""

    timestamp: msgspex.Option[msgspex.isodatetime] = msgspex.field(default=..., converter=msgspex.From[str | datetime | None])


__all__ = (
    "AuthControllerAuthError",
    "BadRequestError",
    "InternalServerError",
    "SubscriptionsControllerNotFoundError",
)
