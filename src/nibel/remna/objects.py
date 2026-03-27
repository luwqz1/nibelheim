from __future__ import annotations

import typing
from datetime import date, datetime
from uuid import UUID

import kungfu
import msgspec
import msgspex
from kungfu.library.monad.option import NOTHING

from .enums import *


class BulkBase(msgspex.Model, kw_only=True):
    status: msgspex.Option[Status] = msgspex.field(default=..., converter=msgspex.From["Status | None"])
    traffic_limit_bytes: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="trafficLimitBytes", converter=msgspex.From[int | None]
    )
    """Traffic limit in bytes. 0 - unlimited"""

    traffic_limit_strategy: msgspex.Option[TrafficLimitStrategy] = msgspex.field(
        default=..., name="trafficLimitStrategy", converter=msgspex.From["TrafficLimitStrategy | None"]
    )
    """Traffic limit reset strategy"""

    expire_at: msgspex.Option[msgspex.isodatetime] = msgspex.field(default=..., name="expireAt", converter=msgspex.From[str | datetime | None])
    """Expiration date: 2025-01-17T15:38:45.065Z"""

    description: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    telegram_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="telegramId", converter=msgspex.From[int | None])
    email: msgspex.NullableOption[msgspex.Email] = msgspex.field(default=NOTHING, converter=msgspex.From[str | msgspex.Email | None])
    tag: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_]+$", max_length=16)]] = msgspex.field(
        default=NOTHING, converter=msgspex.From[str | None]
    )
    hwid_device_limit: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=NOTHING, name="hwidDeviceLimit", converter=msgspex.From[int | None]
    )


class SnippetRequestBase(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=255)]
    snippet: list[dict[str, typing.Any]]


class CreateUserHwidDeviceBase(msgspex.Model, kw_only=True):
    hwid: str
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])


class RequestBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: msgspex.Option[typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]] = msgspex.field(
        default=..., converter=msgspex.From[str | None]
    )


class CloneSubscriptionPageConfigBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    view_position: int = msgspex.field(name="viewPosition")
    name: str
    config: typing.Any


class ResponseDtoResponseInboundsBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    profile_uuid: UUID = msgspex.field(name="profileUuid", converter=msgspex.From[str | UUID])
    tag: str
    type: str
    network: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    security: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    port: msgspex.NullableOption[int] = msgspex.field(default=NOTHING)
    raw_inbound: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="rawInbound")


class CreateConfigProfileResponseDtoResponseNodesBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: str


class CreateBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    view_position: int = msgspex.field(name="viewPosition")
    name: str


class CreateBase2(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: str
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    favicon_link: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="faviconLink")
    login_url: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="loginUrl")


class FetchIpsResultResponseDtoResponseResultNodesBase(msgspex.Model, kw_only=True):
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    node_name: str = msgspex.field(name="nodeName")
    country_code: str = msgspex.field(name="countryCode")


class NodesBase(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    node_name: str = msgspex.field(name="nodeName")
    country_code: str = msgspex.field(name="countryCode")
    config_profile_uuid: UUID = msgspex.field(name="configProfileUuid", converter=msgspex.From[str | UUID])
    config_profile_name: str = msgspex.field(name="configProfileName")


class RemnawaveSettingsResponseDtoResponseOauth2SettingsBase(msgspex.Model, kw_only=True):
    enabled: bool
    client_id: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="clientId")
    client_secret: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="clientSecret")


class UsageBase(msgspex.Model, kw_only=True):
    categories: list[str]
    sparkline_data: list[int] = msgspex.field(name="sparklineData")


class BulkAllExtendExpirationDateRequestDto(msgspex.Model, kw_only=True):
    extend_days: typing.Annotated[int, msgspec.Meta(ge=1)] = msgspex.field(name="extendDays")


class BulkAllUpdateUsersRequestDto(BulkBase, kw_only=True):
    pass


class BulkDeleteHostsRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkDeleteUsersByStatusRequestDto(msgspex.Model, kw_only=True):
    status: msgspex.Option[Status] = msgspex.field(default=..., converter=msgspex.From["Status | None"])


class BulkDeleteUsersRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkDisableHostsRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkEnableHostsRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkExtendExpirationDateRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    extend_days: typing.Annotated[int, msgspec.Meta(ge=1, le=9999)] = msgspex.field(name="extendDays")


class BulkNodesActionsRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1)] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    action: BulkNodesActionsRequestDtoAction


class BulkResetTrafficUsersRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkRevokeUsersSubscriptionRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class BulkUpdateUsersRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    fields: BulkUpdateUsersRequestDtoFields


class BulkUpdateUsersSquadsRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1, max_length=500)] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    active_internal_squads: list[UUID] = msgspex.field(name="activeInternalSquads", converter=msgspex.From[list[str | UUID]])


class CloneSubscriptionPageConfigRequestDto(msgspex.Model, kw_only=True):
    clone_from_uuid: UUID = msgspex.field(name="cloneFromUuid", converter=msgspex.From[str | UUID])


class CreateApiTokenRequestDto(msgspex.Model, kw_only=True):
    token_name: str = msgspex.field(name="tokenName")


class CreateConfigProfileRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]
    config: dict[str, typing.Any]


class CreateExternalSquadRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]


class CreateHostRequestDto(msgspex.Model, kw_only=True):
    inbound: CreateHostRequestDtoInbound
    remark: typing.Annotated[str, msgspec.Meta(min_length=1, max_length=40)]
    address: str
    port: int
    path: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    sni: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    host: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    alpn: msgspex.NullableOption[HostRequestDtoAlpn] = msgspex.field(default=NOTHING, converter=msgspex.From["HostRequestDtoAlpn | None"])
    fingerprint: msgspex.NullableOption[HostRequestDtoFingerprint] = msgspex.field(default=NOTHING, converter=msgspex.From["HostRequestDtoFingerprint | None"])
    is_disabled: msgspex.Option[bool] = msgspex.field(default=..., name="isDisabled", converter=msgspex.From[bool | None])
    security_layer: msgspex.Option[SecurityLayer] = msgspex.field(default=..., name="securityLayer", converter=msgspex.From["SecurityLayer | None"])
    x_http_extra_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="xHttpExtraParams", converter=msgspex.From[typing.Any | None])
    mux_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="muxParams", converter=msgspex.From[typing.Any | None])
    sockopt_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="sockoptParams", converter=msgspex.From[typing.Any | None])
    server_description: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=30)]] = msgspex.field(
        default=NOTHING, name="serverDescription", converter=msgspex.From[str | None]
    )
    tag: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=32)]] = msgspex.field(
        default=NOTHING, converter=msgspex.From[str | None]
    )
    """Optional. Host tag for categorization. Max 32 characters, uppercase letters, numbers, underscores and colons are allowed."""

    is_hidden: msgspex.Option[bool] = msgspex.field(default=..., name="isHidden", converter=msgspex.From[bool | None])
    override_sni_from_address: msgspex.Option[bool] = msgspex.field(default=..., name="overrideSniFromAddress", converter=msgspex.From[bool | None])
    keep_sni_blank: msgspex.Option[bool] = msgspex.field(default=..., name="keepSniBlank", converter=msgspex.From[bool | None])
    allow_insecure: msgspex.Option[bool] = msgspex.field(default=..., name="allowInsecure", converter=msgspex.From[bool | None])
    vless_route_id: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0, le=65535)]] = msgspex.field(
        default=NOTHING, name="vlessRouteId", converter=msgspex.From[int | None]
    )
    shuffle_host: msgspex.Option[bool] = msgspex.field(default=..., name="shuffleHost", converter=msgspex.From[bool | None])
    mihomo_x25519: msgspex.Option[bool] = msgspex.field(default=..., name="mihomoX25519", converter=msgspex.From[bool | None])
    nodes: msgspex.Option[list[UUID]] = msgspex.field(default=..., converter=msgspex.From[list[str | UUID] | None])
    xray_json_template_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="xrayJsonTemplateUuid", converter=msgspex.From[str | UUID | None]
    )
    excluded_internal_squads: msgspex.Option[list[UUID]] = msgspex.field(
        default=..., name="excludedInternalSquads", converter=msgspex.From[list[str | UUID] | None]
    )
    """Optional. Internal squads from which the host will be excluded."""

    exclude_from_subscription_types: msgspex.Option[list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes]] = msgspex.field(
        default=..., name="excludeFromSubscriptionTypes", converter=msgspex.From["list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes] | None"]
    )
    """Optional. Subscription types from which the host will be excluded from."""


class CreateInfraBillingHistoryRecordRequestDto(msgspex.Model, kw_only=True):
    provider_uuid: UUID = msgspex.field(name="providerUuid", converter=msgspex.From[str | UUID])
    amount: typing.Annotated[int, msgspec.Meta(ge=0)]
    billed_at: msgspex.isodatetime = msgspex.field(name="billedAt", converter=msgspex.From[str | datetime])
    """Billing date. Format: 2025-01-17T15:38:45.065Z"""


class CreateInfraBillingNodeRequestDto(msgspex.Model, kw_only=True):
    provider_uuid: UUID = msgspex.field(name="providerUuid", converter=msgspex.From[str | UUID])
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    next_billing_at: msgspex.Option[msgspex.isodatetime] = msgspex.field(default=..., name="nextBillingAt", converter=msgspex.From[str | datetime | None])
    """Next billing date. Format: 2025-01-17T15:38:45.065Z"""


class CreateInfraProviderRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(min_length=2, max_length=30)]
    favicon_link: msgspex.Option[msgspex.URI] = msgspex.field(default=..., name="faviconLink", converter=msgspex.From[str | msgspex.URI | None])
    login_url: msgspex.Option[msgspex.URI] = msgspex.field(default=..., name="loginUrl", converter=msgspex.From[str | msgspex.URI | None])


class CreateInternalSquadRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]
    inbounds: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])


class CreateNodeRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(min_length=3, max_length=30)]
    address: typing.Annotated[str, msgspec.Meta(min_length=2)]
    config_profile: CreateNodeRequestDtoConfigProfile = msgspex.field(name="configProfile")
    port: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=1, le=65535)]] = msgspex.field(default=..., converter=msgspex.From[int | None])
    is_traffic_tracking_active: msgspex.Option[bool] = msgspex.field(default=..., name="isTrafficTrackingActive", converter=msgspex.From[bool | None])
    traffic_limit_bytes: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="trafficLimitBytes", converter=msgspex.From[int | None]
    )
    notify_percent: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0, le=100)]] = msgspex.field(
        default=..., name="notifyPercent", converter=msgspex.From[int | None]
    )
    traffic_reset_day: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=1, le=31)]] = msgspex.field(
        default=..., name="trafficResetDay", converter=msgspex.From[int | None]
    )
    country_code: msgspex.Option[typing.Annotated[str, msgspec.Meta(max_length=2)]] = msgspex.field(
        default=..., name="countryCode", converter=msgspex.From[str | None]
    )
    consumption_multiplier: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0, le=100)]] = msgspex.field(
        default=..., name="consumptionMultiplier", converter=msgspex.From[int | None]
    )
    provider_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="providerUuid", converter=msgspex.From[str | UUID | None])
    tags: msgspex.Option[typing.Annotated[list[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=36)]], msgspec.Meta(max_length=10)]] = (
        msgspex.field(default=..., converter=msgspex.From[list[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=36)]] | None])
    )


class CreateSnippetRequestDto(SnippetRequestBase, kw_only=True):
    pass


class CreateSubscriptionPageConfigRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]


class CreateSubscriptionTemplateRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=255)]
    template_type: BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes = msgspex.field(name="templateType")


class CreateUserHwidDeviceRequestDto(CreateUserHwidDeviceBase, kw_only=True):
    platform: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    os_version: msgspex.Option[str] = msgspex.field(default=..., name="osVersion", converter=msgspex.From[str | None])
    device_model: msgspex.Option[str] = msgspex.field(default=..., name="deviceModel", converter=msgspex.From[str | None])
    user_agent: msgspex.Option[str] = msgspex.field(default=..., name="userAgent", converter=msgspex.From[str | None])


class CreateUserRequestDto(msgspex.Model, kw_only=True):
    username: typing.Annotated[str, msgspec.Meta(pattern=r"^[a-zA-Z0-9_-]+$", min_length=3, max_length=36)]
    """Unique username for the user. Required. Must be 3-36 characters long and contain only letters, numbers, underscores and dashes."""

    expire_at: msgspex.isodatetime = msgspex.field(name="expireAt", converter=msgspex.From[str | datetime])
    """Account expiration date. Required. Format: 2025-01-17T15:38:45.065Z"""

    status: msgspex.Option[CreateUserRequestDtoStatus] = msgspex.field(default=..., converter=msgspex.From["CreateUserRequestDtoStatus | None"])
    """Optional. User account status. Defaults to ACTIVE."""

    short_uuid: msgspex.Option[str] = msgspex.field(default=..., name="shortUuid", converter=msgspex.From[str | None])
    """Optional. Short UUID identifier for the user."""

    trojan_password: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=8, max_length=32)]] = msgspex.field(
        default=..., name="trojanPassword", converter=msgspex.From[str | None]
    )
    """Optional. Password for Trojan protocol. Must be 8-32 characters."""

    vless_uuid: msgspex.Option[UUID] = msgspex.field(default=..., name="vlessUuid", converter=msgspex.From[str | UUID | None])
    """Optional. UUID for VLESS protocol. Must be a valid UUID format."""

    ss_password: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=8, max_length=32)]] = msgspex.field(
        default=..., name="ssPassword", converter=msgspex.From[str | None]
    )
    """Optional. Password for Shadowsocks protocol. Must be 8-32 characters."""

    traffic_limit_bytes: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="trafficLimitBytes", converter=msgspex.From[int | None]
    )
    """Optional. Traffic limit in bytes. Set to 0 for unlimited traffic."""

    traffic_limit_strategy: msgspex.Option[TrafficLimitStrategy2] = msgspex.field(
        default=..., name="trafficLimitStrategy", converter=msgspex.From["TrafficLimitStrategy2 | None"]
    )
    """Available reset periods"""

    created_at: msgspex.Option[msgspex.isodatetime] = msgspex.field(default=..., name="createdAt", converter=msgspex.From[str | datetime | None])
    """Optional. Account creation date. Format: 2025-01-17T15:38:45.065Z"""

    last_traffic_reset_at: msgspex.Option[msgspex.isodatetime] = msgspex.field(
        default=..., name="lastTrafficResetAt", converter=msgspex.From[str | datetime | None]
    )
    """Optional. Date of last traffic reset. Format: 2025-01-17T15:38:45.065Z"""

    description: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    """Optional. Additional notes or description for the user account."""

    tag: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_]+$", max_length=16)]] = msgspex.field(
        default=NOTHING, converter=msgspex.From[str | None]
    )
    """Optional. User tag for categorization. Max 16 characters, uppercase letters, numbers and underscores only."""

    telegram_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="telegramId", converter=msgspex.From[int | None])
    """Optional. Telegram user ID for notifications. Must be an integer."""

    email: msgspex.NullableOption[msgspex.Email] = msgspex.field(default=NOTHING, converter=msgspex.From[str | msgspex.Email | None])
    """Optional. User email address. Must be a valid email format."""

    hwid_device_limit: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="hwidDeviceLimit", converter=msgspex.From[int | None]
    )
    """Optional. Maximum number of hardware devices allowed. Must be a positive integer."""

    active_internal_squads: msgspex.Option[list[UUID]] = msgspex.field(
        default=..., name="activeInternalSquads", converter=msgspex.From[list[str | UUID] | None]
    )
    """Optional. Array of UUIDs representing enabled internal squads."""

    uuid: msgspex.Option[UUID] = msgspex.field(default=..., converter=msgspex.From[str | UUID | None])
    """Optional. Pass UUID to create user with specific UUID, otherwise it will be generated automatically."""

    external_squad_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="externalSquadUuid", converter=msgspex.From[str | UUID | None])
    """Optional. External squad UUID."""


class DebugSrrMatcherRequestDto(msgspex.Model, kw_only=True):
    response_rules: DebugSrrMatcherRequestDtoResponseRules = msgspex.field(name="responseRules")


class DeleteAllUserHwidDevicesRequestDto(msgspex.Model, kw_only=True):
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])


class DeletePasskeyRequestDto(msgspex.Model, kw_only=True):
    id: str


class DeleteSnippetRequestDto(msgspex.Model, kw_only=True):
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=255)]


class DeleteUserHwidDeviceRequestDto(msgspex.Model, kw_only=True):
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])
    hwid: str


class DropConnectionsRequestDto(msgspex.Model, kw_only=True):
    drop_by: kungfu.Sum[DropConnectionsRequestDtoDropBy, DropConnectionsRequestDtoDropBy2] = msgspex.field(
        name="dropBy", converter=msgspex.From["DropConnectionsRequestDtoDropBy | DropConnectionsRequestDtoDropBy2"]
    )
    target_nodes: kungfu.Sum[DropConnectionsRequestDtoTargetNodes, DropConnectionsRequestDtoTargetNodes2] = msgspex.field(
        name="targetNodes", converter=msgspex.From["DropConnectionsRequestDtoTargetNodes | DropConnectionsRequestDtoTargetNodes2"]
    )


class EncryptHappCryptoLinkRequestDto(msgspex.Model, kw_only=True):
    link_to_encrypt: msgspex.URI = msgspex.field(name="linkToEncrypt", converter=msgspex.From[str | msgspex.URI])


class LoginRequestDto(msgspex.Model, kw_only=True):
    username: str
    password: str


class OAuth2AuthorizeRequestDto(msgspex.Model, kw_only=True):
    provider: RequestDtoProvider


class OAuth2CallbackRequestDto(msgspex.Model, kw_only=True):
    provider: RequestDtoProvider
    code: str
    state: str


class ProfileModificationRequestDto(msgspex.Model, kw_only=True):
    uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1)] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    config_profile: CreateNodeRequestDtoConfigProfile = msgspex.field(name="configProfile")


class RegisterRequestDto(msgspex.Model, kw_only=True):
    username: str
    password: typing.Annotated[str, msgspec.Meta(pattern=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{24,}$", min_length=24)]


class RemnawaveWebhookCrmEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookCrmEventsDtoScope
    event: RemnawaveWebhookCrmEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: RemnawaveWebhookCrmEventsDtoData


class RemnawaveWebhookErrorsEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookErrorsEventsDtoScope
    event: RemnawaveWebhookErrorsEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: RemnawaveWebhookErrorsEventsDtoData


class RemnawaveWebhookNodeEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookNodeEventsDtoScope
    event: RemnawaveWebhookNodeEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: CreateNodeResponseDtoResponse


class RemnawaveWebhookServiceEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookServiceEventsDtoScope
    event: RemnawaveWebhookServiceEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: RemnawaveWebhookServiceEventsDtoData


class RemnawaveWebhookUserEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookUserEventsDtoScope
    event: RemnawaveWebhookUserEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: CreateUserResponseDtoResponse
    meta: msgspex.NullableOption[RemnawaveWebhookUserEventsDtoMeta] = msgspex.field(default=NOTHING)


class RemnawaveWebhookUserHwidDevicesEventsDto(msgspex.Model, kw_only=True):
    scope: RemnawaveWebhookUserHwidDevicesEventsDtoScope
    event: RemnawaveWebhookUserHwidDevicesEventsDtoEvent
    timestamp: msgspex.isodatetime = msgspex.field(converter=msgspex.From[str | datetime])
    data: RemnawaveWebhookUserHwidDevicesEventsDtoData


class ReorderConfigProfilesRequestDto(msgspex.Model, kw_only=True):
    items: list[ReorderConfigProfilesRequestDtoItems]


class ReorderExternalSquadsRequestDto(msgspex.Model, kw_only=True):
    items: list[ReorderConfigProfilesRequestDtoItems]


class ReorderHostRequestDto(msgspex.Model, kw_only=True):
    hosts: list[ReorderConfigProfilesRequestDtoItems]


class ReorderInternalSquadsRequestDto(msgspex.Model, kw_only=True):
    items: list[ReorderConfigProfilesRequestDtoItems]


class ReorderNodeRequestDto(msgspex.Model, kw_only=True):
    nodes: list[ReorderConfigProfilesRequestDtoItems]


class ReorderSubscriptionPageConfigsRequestDto(msgspex.Model, kw_only=True):
    items: list[ReorderConfigProfilesRequestDtoItems]


class ReorderSubscriptionTemplatesRequestDto(msgspex.Model, kw_only=True):
    items: list[ReorderConfigProfilesRequestDtoItems]


class RestartAllNodesRequestBodyDto(msgspex.Model, kw_only=True):
    force_restart: msgspex.Option[bool] = msgspex.field(default=..., name="forceRestart", converter=msgspex.From[bool | None])


class SetInboundToManyHostsRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    config_profile_uuid: UUID = msgspex.field(name="configProfileUuid", converter=msgspex.From[str | UUID])
    config_profile_inbound_uuid: UUID = msgspex.field(name="configProfileInboundUuid", converter=msgspex.From[str | UUID])


class SetPortToManyHostsRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    port: typing.Annotated[int, msgspec.Meta(ge=1, le=65535)]


class TelegramCallbackRequestDto(msgspex.Model, kw_only=True):
    id: int
    first_name: str
    auth_date: int
    hash: str
    last_name: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    username: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    photo_url: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])


class UpdateConfigProfileRequestDto(RequestBase, kw_only=True):
    config: msgspex.Option[dict[str, typing.Any]] = msgspex.field(default=..., converter=msgspex.From[dict[str, typing.Any] | None])


class UpdateExternalSquadRequestDto(RequestBase, kw_only=True):
    templates: msgspex.Option[list[CreateExternalSquadResponseDtoResponseTemplates]] = msgspex.field(
        default=..., converter=msgspex.From["list[CreateExternalSquadResponseDtoResponseTemplates] | None"]
    )
    subscription_settings: msgspex.Option[CreateExternalSquadResponseDtoResponseSubscriptionSettings] = msgspex.field(
        default=..., name="subscriptionSettings", converter=msgspex.From["CreateExternalSquadResponseDtoResponseSubscriptionSettings | None"]
    )
    host_overrides: msgspex.Option[CreateExternalSquadResponseDtoResponseHostOverrides] = msgspex.field(
        default=..., name="hostOverrides", converter=msgspex.From["CreateExternalSquadResponseDtoResponseHostOverrides | None"]
    )
    response_headers: msgspex.NullableOption[dict[str, str]] = msgspex.field(
        default=NOTHING, name="responseHeaders", converter=msgspex.From[dict[str, str] | None]
    )
    hwid_settings: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseHwidSettings] = msgspex.field(
        default=NOTHING, name="hwidSettings", converter=msgspex.From["CreateExternalSquadResponseDtoResponseHwidSettings | None"]
    )
    custom_remarks: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseCustomRemarks] = msgspex.field(
        default=NOTHING, name="customRemarks", converter=msgspex.From["CreateExternalSquadResponseDtoResponseCustomRemarks | None"]
    )
    subpage_config_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="subpageConfigUuid", converter=msgspex.From[str | UUID | None])


class UpdateHostRequestDto(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    inbound: msgspex.Option[CreateHostRequestDtoInbound] = msgspex.field(default=..., converter=msgspex.From["CreateHostRequestDtoInbound | None"])
    remark: msgspex.Option[typing.Annotated[str, msgspec.Meta(max_length=40)]] = msgspex.field(default=..., converter=msgspex.From[str | None])
    address: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    port: msgspex.Option[int] = msgspex.field(default=..., converter=msgspex.From[int | None])
    path: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    sni: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    host: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    alpn: msgspex.NullableOption[HostRequestDtoAlpn] = msgspex.field(default=NOTHING, converter=msgspex.From["HostRequestDtoAlpn | None"])
    fingerprint: msgspex.NullableOption[HostRequestDtoFingerprint] = msgspex.field(default=NOTHING, converter=msgspex.From["HostRequestDtoFingerprint | None"])
    is_disabled: msgspex.Option[bool] = msgspex.field(default=..., name="isDisabled", converter=msgspex.From[bool | None])
    security_layer: msgspex.Option[SecurityLayer] = msgspex.field(default=..., name="securityLayer", converter=msgspex.From["SecurityLayer | None"])
    x_http_extra_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="xHttpExtraParams", converter=msgspex.From[typing.Any | None])
    mux_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="muxParams", converter=msgspex.From[typing.Any | None])
    sockopt_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="sockoptParams", converter=msgspex.From[typing.Any | None])
    server_description: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=30)]] = msgspex.field(
        default=NOTHING, name="serverDescription", converter=msgspex.From[str | None]
    )
    tag: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=32)]] = msgspex.field(
        default=NOTHING, converter=msgspex.From[str | None]
    )
    """Optional. Host tag for categorization. Max 32 characters, uppercase letters, numbers, underscores and colons are allowed."""

    is_hidden: msgspex.Option[bool] = msgspex.field(default=..., name="isHidden", converter=msgspex.From[bool | None])
    override_sni_from_address: msgspex.Option[bool] = msgspex.field(default=..., name="overrideSniFromAddress", converter=msgspex.From[bool | None])
    keep_sni_blank: msgspex.Option[bool] = msgspex.field(default=..., name="keepSniBlank", converter=msgspex.From[bool | None])
    vless_route_id: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0, le=65535)]] = msgspex.field(
        default=NOTHING, name="vlessRouteId", converter=msgspex.From[int | None]
    )
    allow_insecure: msgspex.Option[bool] = msgspex.field(default=..., name="allowInsecure", converter=msgspex.From[bool | None])
    shuffle_host: msgspex.Option[bool] = msgspex.field(default=..., name="shuffleHost", converter=msgspex.From[bool | None])
    mihomo_x25519: msgspex.Option[bool] = msgspex.field(default=..., name="mihomoX25519", converter=msgspex.From[bool | None])
    nodes: msgspex.Option[list[UUID]] = msgspex.field(default=..., converter=msgspex.From[list[str | UUID] | None])
    xray_json_template_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="xrayJsonTemplateUuid", converter=msgspex.From[str | UUID | None]
    )
    excluded_internal_squads: msgspex.Option[list[UUID]] = msgspex.field(
        default=..., name="excludedInternalSquads", converter=msgspex.From[list[str | UUID] | None]
    )
    """Optional. Internal squads from which the host will be excluded."""

    exclude_from_subscription_types: msgspex.Option[list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes]] = msgspex.field(
        default=..., name="excludeFromSubscriptionTypes", converter=msgspex.From["list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes] | None"]
    )
    """Optional. Subscription types from which the host will be excluded from."""


class UpdateInfraBillingNodeRequestDto(msgspex.Model, kw_only=True):
    uuids: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    next_billing_at: msgspex.isodatetime = msgspex.field(name="nextBillingAt", converter=msgspex.From[str | datetime])


class UpdateInfraProviderRequestDto(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=2, max_length=30)]] = msgspex.field(default=..., converter=msgspex.From[str | None])
    favicon_link: msgspex.NullableOption[msgspex.URI] = msgspex.field(default=NOTHING, name="faviconLink", converter=msgspex.From[str | msgspex.URI | None])
    login_url: msgspex.NullableOption[msgspex.URI] = msgspex.field(default=NOTHING, name="loginUrl", converter=msgspex.From[str | msgspex.URI | None])


class UpdateInternalSquadRequestDto(RequestBase, kw_only=True):
    inbounds: msgspex.Option[list[UUID]] = msgspex.field(default=..., converter=msgspex.From[list[str | UUID] | None])


class UpdateNodeRequestDto(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=3, max_length=30)]] = msgspex.field(default=..., converter=msgspex.From[str | None])
    address: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=2)]] = msgspex.field(default=..., converter=msgspex.From[str | None])
    port: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=1, le=65535)]] = msgspex.field(default=..., converter=msgspex.From[int | None])
    is_traffic_tracking_active: msgspex.Option[bool] = msgspex.field(default=..., name="isTrafficTrackingActive", converter=msgspex.From[bool | None])
    traffic_limit_bytes: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="trafficLimitBytes", converter=msgspex.From[int | None]
    )
    notify_percent: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0, le=100)]] = msgspex.field(
        default=..., name="notifyPercent", converter=msgspex.From[int | None]
    )
    traffic_reset_day: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=1, le=31)]] = msgspex.field(
        default=..., name="trafficResetDay", converter=msgspex.From[int | None]
    )
    country_code: msgspex.Option[typing.Annotated[str, msgspec.Meta(max_length=2)]] = msgspex.field(
        default=..., name="countryCode", converter=msgspex.From[str | None]
    )
    consumption_multiplier: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0, le=100)]] = msgspex.field(
        default=..., name="consumptionMultiplier", converter=msgspex.From[int | None]
    )
    config_profile: msgspex.Option[CreateNodeRequestDtoConfigProfile] = msgspex.field(
        default=..., name="configProfile", converter=msgspex.From["CreateNodeRequestDtoConfigProfile | None"]
    )
    provider_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="providerUuid", converter=msgspex.From[str | UUID | None])
    tags: msgspex.Option[typing.Annotated[list[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=36)]], msgspec.Meta(max_length=10)]] = (
        msgspex.field(default=..., converter=msgspex.From[list[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_:]+$", max_length=36)]] | None])
    )


class UpdatePasskeyRequestDto(msgspex.Model, kw_only=True):
    id: str
    name: typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=30)]


class UpdateRemnawaveSettingsRequestDto(msgspex.Model, kw_only=True):
    passkey_settings: msgspex.Option[GetRemnawaveSettingsResponseDtoResponsePasskeySettings] = msgspex.field(
        default=..., name="passkeySettings", converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponsePasskeySettings | None"]
    )
    oauth2_settings: msgspex.Option[GetRemnawaveSettingsResponseDtoResponseOauth2Settings] = msgspex.field(
        default=..., name="oauth2Settings", converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponseOauth2Settings | None"]
    )
    tg_auth_settings: msgspex.Option[GetRemnawaveSettingsResponseDtoResponseTgAuthSettings] = msgspex.field(
        default=..., name="tgAuthSettings", converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponseTgAuthSettings | None"]
    )
    password_settings: msgspex.Option[GetRemnawaveSettingsResponseDtoResponsePasswordSettings] = msgspex.field(
        default=..., name="passwordSettings", converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponsePasswordSettings | None"]
    )
    branding_settings: msgspex.Option[GetRemnawaveSettingsResponseDtoResponseBrandingSettings] = msgspex.field(
        default=..., name="brandingSettings", converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponseBrandingSettings | None"]
    )


class UpdateSnippetRequestDto(SnippetRequestBase, kw_only=True):
    pass


class UpdateSubscriptionPageConfigRequestDto(RequestBase, kw_only=True):
    config: msgspex.Option[typing.Any] = msgspex.field(default=..., converter=msgspex.From[typing.Any | None])


class UpdateSubscriptionSettingsRequestDto(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    profile_title: msgspex.Option[str] = msgspex.field(default=..., name="profileTitle", converter=msgspex.From[str | None])
    support_link: msgspex.Option[str] = msgspex.field(default=..., name="supportLink", converter=msgspex.From[str | None])
    profile_update_interval: msgspex.Option[int] = msgspex.field(default=..., name="profileUpdateInterval", converter=msgspex.From[int | None])
    is_profile_webpage_url_enabled: msgspex.Option[bool] = msgspex.field(default=..., name="isProfileWebpageUrlEnabled", converter=msgspex.From[bool | None])
    serve_json_at_base_subscription: msgspex.Option[bool] = msgspex.field(default=..., name="serveJsonAtBaseSubscription", converter=msgspex.From[bool | None])
    happ_announce: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=200)]] = msgspex.field(
        default=NOTHING, name="happAnnounce", converter=msgspex.From[str | None]
    )
    happ_routing: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="happRouting", converter=msgspex.From[str | None])
    is_show_custom_remarks: msgspex.Option[bool] = msgspex.field(default=..., name="isShowCustomRemarks", converter=msgspex.From[bool | None])
    custom_remarks: msgspex.Option[CreateExternalSquadResponseDtoResponseCustomRemarks] = msgspex.field(
        default=..., name="customRemarks", converter=msgspex.From["CreateExternalSquadResponseDtoResponseCustomRemarks | None"]
    )
    custom_response_headers: msgspex.Option[dict[str, str]] = msgspex.field(
        default=..., name="customResponseHeaders", converter=msgspex.From[dict[str, str] | None]
    )
    randomize_hosts: msgspex.Option[bool] = msgspex.field(default=..., name="randomizeHosts", converter=msgspex.From[bool | None])
    response_rules: msgspex.Option[DebugSrrMatcherRequestDtoResponseRules] = msgspex.field(
        default=..., name="responseRules", converter=msgspex.From["DebugSrrMatcherRequestDtoResponseRules | None"]
    )
    hwid_settings: msgspex.Option[CreateExternalSquadResponseDtoResponseHwidSettings] = msgspex.field(
        default=..., name="hwidSettings", converter=msgspex.From["CreateExternalSquadResponseDtoResponseHwidSettings | None"]
    )


class UpdateTemplateRequestDto(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: msgspex.Option[typing.Annotated[str, msgspec.Meta(pattern="^[A-Za-z0-9_\\s-]+$", min_length=2, max_length=255)]] = msgspex.field(
        default=..., converter=msgspex.From[str | None]
    )
    template_json: msgspex.Option[dict[str, typing.Any]] = msgspex.field(default=..., name="templateJson", converter=msgspex.From[dict[str, typing.Any] | None])
    encoded_template_yaml: msgspex.Option[str] = msgspex.field(default=..., name="encodedTemplateYaml", converter=msgspex.From[str | None])


class UpdateUserRequestDto(msgspex.Model, kw_only=True):
    username: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    """Username of the user"""

    uuid: msgspex.Option[UUID] = msgspex.field(default=..., converter=msgspex.From[str | UUID | None])
    """UUID of the user. UUID has higher priority than username, so if both are provided, username will be ignored."""

    status: msgspex.Option[UpdateUserRequestDtoStatus] = msgspex.field(default=..., converter=msgspex.From["UpdateUserRequestDtoStatus | None"])
    traffic_limit_bytes: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=..., name="trafficLimitBytes", converter=msgspex.From[int | None]
    )
    """Traffic limit in bytes. 0 - unlimited"""

    traffic_limit_strategy: msgspex.Option[TrafficLimitStrategy2] = msgspex.field(
        default=..., name="trafficLimitStrategy", converter=msgspex.From["TrafficLimitStrategy2 | None"]
    )
    """Available reset periods"""

    expire_at: msgspex.Option[msgspex.isodatetime] = msgspex.field(default=..., name="expireAt", converter=msgspex.From[str | datetime | None])
    """Expiration date: 2025-01-17T15:38:45.065Z"""

    description: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    tag: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(pattern=r"^[A-Z0-9_]+$", max_length=16)]] = msgspex.field(
        default=NOTHING, converter=msgspex.From[str | None]
    )
    telegram_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="telegramId", converter=msgspex.From[int | None])
    email: msgspex.NullableOption[msgspex.Email] = msgspex.field(default=NOTHING, converter=msgspex.From[str | msgspex.Email | None])
    hwid_device_limit: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0)]] = msgspex.field(
        default=NOTHING, name="hwidDeviceLimit", converter=msgspex.From[int | None]
    )
    active_internal_squads: msgspex.Option[list[UUID]] = msgspex.field(
        default=..., name="activeInternalSquads", converter=msgspex.From[list[str | UUID] | None]
    )
    external_squad_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="externalSquadUuid", converter=msgspex.From[str | UUID | None])
    """Optional. External squad UUID."""


class VerifyPasskeyAuthenticationRequestDto(msgspex.Model, kw_only=True):
    response: typing.Any


class VerifyPasskeyRegistrationRequestDto(msgspex.Model, kw_only=True):
    response: typing.Any


class AddUsersToExternalSquadResponseDtoResponse(msgspex.Model, kw_only=True):
    event_sent: bool = msgspex.field(name="eventSent")


class BulkDeleteHostsResponseDtoResponseInbound(msgspex.Model, kw_only=True):
    config_profile_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="configProfileUuid", converter=msgspex.From[str | UUID | None])
    config_profile_inbound_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="configProfileInboundUuid", converter=msgspex.From[str | UUID | None]
    )


class BulkDeleteHostsResponseDtoResponse(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    view_position: int = msgspex.field(name="viewPosition")
    remark: str
    address: str
    port: int
    inbound: BulkDeleteHostsResponseDtoResponseInbound
    shuffle_host: bool = msgspex.field(name="shuffleHost")
    mihomo_x25519: bool = msgspex.field(name="mihomoX25519")
    nodes: list[UUID] = msgspex.field(converter=msgspex.From[list[str | UUID]])
    excluded_internal_squads: list[UUID] = msgspex.field(name="excludedInternalSquads", converter=msgspex.From[list[str | UUID]])
    path: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    sni: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    host: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    alpn: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    fingerprint: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    is_disabled: msgspex.Option[bool] = msgspex.field(default=..., name="isDisabled", converter=msgspex.From[bool | None])
    security_layer: msgspex.Option[SecurityLayer] = msgspex.field(default=..., name="securityLayer", converter=msgspex.From["SecurityLayer | None"])
    x_http_extra_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="xHttpExtraParams")
    mux_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="muxParams")
    sockopt_params: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="sockoptParams")
    server_description: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=30)]] = msgspex.field(default=NOTHING, name="serverDescription")
    tag: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    is_hidden: msgspex.Option[bool] = msgspex.field(default=..., name="isHidden", converter=msgspex.From[bool | None])
    override_sni_from_address: msgspex.Option[bool] = msgspex.field(default=..., name="overrideSniFromAddress", converter=msgspex.From[bool | None])
    keep_sni_blank: msgspex.Option[bool] = msgspex.field(default=..., name="keepSniBlank", converter=msgspex.From[bool | None])
    vless_route_id: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0, le=65535)]] = msgspex.field(default=NOTHING, name="vlessRouteId")
    allow_insecure: msgspex.Option[bool] = msgspex.field(default=..., name="allowInsecure", converter=msgspex.From[bool | None])
    xray_json_template_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="xrayJsonTemplateUuid", converter=msgspex.From[str | UUID | None]
    )
    exclude_from_subscription_types: msgspex.Option[list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes]] = msgspex.field(
        default=..., name="excludeFromSubscriptionTypes", converter=msgspex.From["list[BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes] | None"]
    )


class BulkDeleteUsersByStatusResponseDtoResponse(msgspex.Model, kw_only=True):
    affected_rows: int = msgspex.field(name="affectedRows")


class BulkUpdateUsersRequestDtoFields(BulkBase, kw_only=True):
    external_squad_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="externalSquadUuid", converter=msgspex.From[str | UUID | None])
    """Optional. External squad UUID."""


class CloneSubscriptionPageConfigResponseDtoResponse(CloneSubscriptionPageConfigBase, kw_only=True):
    pass


class CreateApiTokenResponseDtoResponse(msgspex.Model, kw_only=True):
    token: str
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])


class CreateConfigProfileResponseDtoResponseInbounds(ResponseDtoResponseInboundsBase, kw_only=True):
    pass


class CreateConfigProfileResponseDtoResponseNodes(CreateConfigProfileResponseDtoResponseNodesBase, kw_only=True):
    country_code: str = msgspex.field(name="countryCode")


class CreateConfigProfileResponseDtoResponse(CloneSubscriptionPageConfigBase, kw_only=True):
    inbounds: list[CreateConfigProfileResponseDtoResponseInbounds]
    nodes: list[CreateConfigProfileResponseDtoResponseNodes]
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])


class CreateExternalSquadResponseDtoResponseInfo(msgspex.Model, kw_only=True):
    members_count: int = msgspex.field(name="membersCount")


class CreateExternalSquadResponseDtoResponseTemplates(msgspex.Model, kw_only=True):
    template_uuid: UUID = msgspex.field(name="templateUuid", converter=msgspex.From[str | UUID])
    template_type: BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes = msgspex.field(name="templateType")


class CreateExternalSquadResponseDtoResponseSubscriptionSettings(msgspex.Model, kw_only=True):
    profile_title: msgspex.Option[str] = msgspex.field(default=..., name="profileTitle", converter=msgspex.From[str | None])
    support_link: msgspex.Option[str] = msgspex.field(default=..., name="supportLink", converter=msgspex.From[str | None])
    profile_update_interval: msgspex.Option[typing.Annotated[int, msgspec.Meta(ge=1)]] = msgspex.field(
        default=..., name="profileUpdateInterval", converter=msgspex.From[int | None]
    )
    is_profile_webpage_url_enabled: msgspex.Option[bool] = msgspex.field(default=..., name="isProfileWebpageUrlEnabled", converter=msgspex.From[bool | None])
    serve_json_at_base_subscription: msgspex.Option[bool] = msgspex.field(default=..., name="serveJsonAtBaseSubscription", converter=msgspex.From[bool | None])
    is_show_custom_remarks: msgspex.Option[bool] = msgspex.field(default=..., name="isShowCustomRemarks", converter=msgspex.From[bool | None])
    happ_announce: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="happAnnounce", converter=msgspex.From[str | None])
    happ_routing: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="happRouting", converter=msgspex.From[str | None])
    randomize_hosts: msgspex.Option[bool] = msgspex.field(default=..., name="randomizeHosts", converter=msgspex.From[bool | None])


class CreateExternalSquadResponseDtoResponseHostOverrides(msgspex.Model, kw_only=True):
    server_description: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=30)]] = msgspex.field(
        default=NOTHING, name="serverDescription", converter=msgspex.From[str | None]
    )
    vless_route_id: msgspex.NullableOption[typing.Annotated[int, msgspec.Meta(ge=0, le=65535)]] = msgspex.field(
        default=NOTHING, name="vlessRouteId", converter=msgspex.From[int | None]
    )


class CreateExternalSquadResponseDtoResponseHwidSettings(msgspex.Model, kw_only=True):
    enabled: bool
    fallback_device_limit: int = msgspex.field(name="fallbackDeviceLimit")
    max_devices_announce: msgspex.NullableOption[typing.Annotated[str, msgspec.Meta(max_length=200)]] = msgspex.field(
        default=NOTHING, name="maxDevicesAnnounce"
    )


class CreateExternalSquadResponseDtoResponseCustomRemarks(msgspex.Model, kw_only=True):
    expired_users: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="expiredUsers")
    limited_users: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="limitedUsers")
    disabled_users: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="disabledUsers")
    empty_hosts: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="emptyHosts")
    hwid_max_devices_exceeded: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="HWIDMaxDevicesExceeded")
    hwid_not_supported: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="HWIDNotSupported")


class CreateExternalSquadResponseDtoResponse(CreateBase, kw_only=True):
    info: CreateExternalSquadResponseDtoResponseInfo
    templates: list[CreateExternalSquadResponseDtoResponseTemplates]
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    subscription_settings: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseSubscriptionSettings] = msgspex.field(
        default=NOTHING, name="subscriptionSettings"
    )
    host_overrides: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseHostOverrides] = msgspex.field(default=NOTHING, name="hostOverrides")
    response_headers: msgspex.NullableOption[dict[str, str]] = msgspex.field(default=NOTHING, name="responseHeaders")
    hwid_settings: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseHwidSettings] = msgspex.field(default=NOTHING, name="hwidSettings")
    custom_remarks: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseCustomRemarks] = msgspex.field(default=NOTHING, name="customRemarks")
    subpage_config_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="subpageConfigUuid", converter=msgspex.From[str | UUID | None])


class CreateHostRequestDtoInbound(msgspex.Model, kw_only=True):
    config_profile_uuid: UUID = msgspex.field(name="configProfileUuid", converter=msgspex.From[str | UUID])
    config_profile_inbound_uuid: UUID = msgspex.field(name="configProfileInboundUuid", converter=msgspex.From[str | UUID])


class CreateInfraBillingHistoryRecordResponseDtoResponseRecordsProvider(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    name: str
    favicon_link: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="faviconLink")


class CreateInfraBillingHistoryRecordResponseDtoResponseRecords(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    provider_uuid: UUID = msgspex.field(name="providerUuid", converter=msgspex.From[str | UUID])
    amount: int
    billed_at: msgspex.isodatetime = msgspex.field(name="billedAt", converter=msgspex.From[str | datetime])
    provider: CreateInfraBillingHistoryRecordResponseDtoResponseRecordsProvider


class CreateInfraBillingHistoryRecordResponseDtoResponse(msgspex.Model, kw_only=True):
    records: list[CreateInfraBillingHistoryRecordResponseDtoResponseRecords]
    total: int


class CreateInfraBillingNodeResponseDtoResponseBillingNodesProvider(CreateConfigProfileResponseDtoResponseNodesBase, kw_only=True):
    login_url: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="loginUrl")
    favicon_link: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="faviconLink")


class CreateInfraBillingNodeResponseDtoResponseBillingNodes(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    provider_uuid: UUID = msgspex.field(name="providerUuid", converter=msgspex.From[str | UUID])
    provider: CreateInfraBillingNodeResponseDtoResponseBillingNodesProvider
    node: CreateConfigProfileResponseDtoResponseNodes
    next_billing_at: msgspex.isodatetime = msgspex.field(name="nextBillingAt", converter=msgspex.From[str | datetime])
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])


class CreateInfraBillingNodeResponseDtoResponseStats(msgspex.Model, kw_only=True):
    upcoming_nodes_count: int = msgspex.field(name="upcomingNodesCount")
    current_month_payments: int = msgspex.field(name="currentMonthPayments")
    total_spent: int = msgspex.field(name="totalSpent")


class CreateInfraBillingNodeResponseDtoResponse(msgspex.Model, kw_only=True):
    total_billing_nodes: int = msgspex.field(name="totalBillingNodes")
    billing_nodes: list[CreateInfraBillingNodeResponseDtoResponseBillingNodes] = msgspex.field(name="billingNodes")
    available_billing_nodes: list[CreateConfigProfileResponseDtoResponseNodes] = msgspex.field(name="availableBillingNodes")
    total_available_billing_nodes: int = msgspex.field(name="totalAvailableBillingNodes")
    stats: CreateInfraBillingNodeResponseDtoResponseStats


class CreateInfraProviderResponseDtoResponseBillingHistory(msgspex.Model, kw_only=True):
    total_amount: int = msgspex.field(name="totalAmount")
    total_bills: int = msgspex.field(name="totalBills")


class CreateInfraProviderResponseDtoResponseBillingNodes(msgspex.Model, kw_only=True):
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    name: str
    country_code: str = msgspex.field(name="countryCode")


class CreateInfraProviderResponseDtoResponse(CreateBase2, kw_only=True):
    billing_history: CreateInfraProviderResponseDtoResponseBillingHistory = msgspex.field(name="billingHistory")
    billing_nodes: list[CreateInfraProviderResponseDtoResponseBillingNodes] = msgspex.field(name="billingNodes")


class CreateInternalSquadResponseDtoResponseInfo(msgspex.Model, kw_only=True):
    members_count: int = msgspex.field(name="membersCount")
    inbounds_count: int = msgspex.field(name="inboundsCount")


class CreateInternalSquadResponseDtoResponse(CreateBase, kw_only=True):
    info: CreateInternalSquadResponseDtoResponseInfo
    inbounds: list[CreateConfigProfileResponseDtoResponseInbounds]
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])


class CreateNodeRequestDtoConfigProfile(msgspex.Model, kw_only=True):
    active_config_profile_uuid: UUID = msgspex.field(name="activeConfigProfileUuid", converter=msgspex.From[str | UUID])
    active_inbounds: list[UUID] = msgspex.field(name="activeInbounds", converter=msgspex.From[list[str | UUID]])


class CreateNodeResponseDtoResponseConfigProfile(msgspex.Model, kw_only=True):
    active_inbounds: list[CreateConfigProfileResponseDtoResponseInbounds] = msgspex.field(name="activeInbounds")
    active_config_profile_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="activeConfigProfileUuid", converter=msgspex.From[str | UUID | None]
    )


class CreateNodeResponseDtoResponseProvider(CreateBase2, kw_only=True):
    pass


class CreateNodeResponseDtoResponse(CreateConfigProfileResponseDtoResponseNodesBase, kw_only=True):
    address: str
    is_connected: bool = msgspex.field(name="isConnected")
    is_disabled: bool = msgspex.field(name="isDisabled")
    is_connecting: bool = msgspex.field(name="isConnecting")
    xray_uptime: str = msgspex.field(name="xrayUptime")
    is_traffic_tracking_active: bool = msgspex.field(name="isTrafficTrackingActive")
    view_position: int = msgspex.field(name="viewPosition")
    country_code: str = msgspex.field(name="countryCode")
    consumption_multiplier: int = msgspex.field(name="consumptionMultiplier")
    tags: list[str]
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    config_profile: CreateNodeResponseDtoResponseConfigProfile = msgspex.field(name="configProfile")
    port: msgspex.NullableOption[int] = msgspex.field(default=NOTHING)
    last_status_change: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(
        default=NOTHING, name="lastStatusChange", converter=msgspex.From[str | datetime | None]
    )
    last_status_message: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="lastStatusMessage")
    xray_version: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="xrayVersion")
    node_version: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="nodeVersion")
    traffic_reset_day: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="trafficResetDay")
    traffic_limit_bytes: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="trafficLimitBytes")
    traffic_used_bytes: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="trafficUsedBytes")
    notify_percent: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="notifyPercent")
    users_online: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="usersOnline")
    cpu_count: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="cpuCount")
    cpu_model: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="cpuModel")
    total_ram: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="totalRam")
    provider_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="providerUuid", converter=msgspex.From[str | UUID | None])
    provider: msgspex.NullableOption[CreateNodeResponseDtoResponseProvider] = msgspex.field(default=NOTHING)


class CreateSnippetResponseDtoResponseSnippets(msgspex.Model, kw_only=True):
    name: str
    snippet: typing.Any


class CreateSnippetResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    snippets: list[CreateSnippetResponseDtoResponseSnippets]


class CreateSubscriptionPageConfigResponseDtoResponse(CreateBase, kw_only=True):
    config: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING)


class CreateSubscriptionTemplateResponseDtoResponse(CreateBase, kw_only=True):
    template_type: BulkDeleteHostsResponseDtoResponseExcludeFromSubscriptionTypes = msgspex.field(name="templateType")
    template_json: msgspex.NullableOption[typing.Any] = msgspex.field(default=NOTHING, name="templateJson")
    encoded_template_yaml: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="encodedTemplateYaml")


class CreateUserHwidDeviceResponseDtoResponseDevices(CreateUserHwidDeviceBase, kw_only=True):
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    platform: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    os_version: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="osVersion")
    device_model: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="deviceModel")
    user_agent: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="userAgent")


class CreateUserHwidDeviceResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    devices: list[CreateUserHwidDeviceResponseDtoResponseDevices]


class CreateUserResponseDtoResponseActiveInternalSquads(CreateConfigProfileResponseDtoResponseNodesBase, kw_only=True):
    pass


class CreateUserResponseDtoResponseUserTraffic(msgspex.Model, kw_only=True):
    used_traffic_bytes: int = msgspex.field(name="usedTrafficBytes")
    lifetime_used_traffic_bytes: int = msgspex.field(name="lifetimeUsedTrafficBytes")
    online_at: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(default=NOTHING, name="onlineAt", converter=msgspex.From[str | datetime | None])
    first_connected_at: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(
        default=NOTHING, name="firstConnectedAt", converter=msgspex.From[str | datetime | None]
    )
    last_connected_node_uuid: msgspex.NullableOption[UUID] = msgspex.field(
        default=NOTHING, name="lastConnectedNodeUuid", converter=msgspex.From[str | UUID | None]
    )


class CreateUserResponseDtoResponse(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    id: int
    short_uuid: str = msgspex.field(name="shortUuid")
    username: str
    expire_at: msgspex.isodatetime = msgspex.field(name="expireAt", converter=msgspex.From[str | datetime])
    trojan_password: str = msgspex.field(name="trojanPassword")
    vless_uuid: UUID = msgspex.field(name="vlessUuid", converter=msgspex.From[str | UUID])
    ss_password: str = msgspex.field(name="ssPassword")
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    subscription_url: str = msgspex.field(name="subscriptionUrl")
    active_internal_squads: list[CreateUserResponseDtoResponseActiveInternalSquads] = msgspex.field(name="activeInternalSquads")
    user_traffic: CreateUserResponseDtoResponseUserTraffic = msgspex.field(name="userTraffic")
    status: msgspex.Option[Status] = msgspex.field(default=..., converter=msgspex.From["Status | None"])
    traffic_limit_bytes: msgspex.Option[int] = msgspex.field(default=..., name="trafficLimitBytes", converter=msgspex.From[int | None])
    traffic_limit_strategy: msgspex.Option[TrafficLimitStrategy2] = msgspex.field(
        default=..., name="trafficLimitStrategy", converter=msgspex.From["TrafficLimitStrategy2 | None"]
    )
    """Available reset periods"""

    telegram_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="telegramId")
    email: msgspex.NullableOption[msgspex.Email] = msgspex.field(default=NOTHING, converter=msgspex.From[str | msgspex.Email | None])
    description: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    tag: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    hwid_device_limit: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="hwidDeviceLimit")
    external_squad_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="externalSquadUuid", converter=msgspex.From[str | UUID | None])
    last_triggered_threshold: msgspex.Option[int] = msgspex.field(default=..., name="lastTriggeredThreshold", converter=msgspex.From[int | None])
    sub_revoked_at: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(
        default=NOTHING, name="subRevokedAt", converter=msgspex.From[str | datetime | None]
    )
    sub_last_user_agent: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="subLastUserAgent")
    sub_last_opened_at: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(
        default=NOTHING, name="subLastOpenedAt", converter=msgspex.From[str | datetime | None]
    )
    last_traffic_reset_at: msgspex.NullableOption[msgspex.isodatetime] = msgspex.field(
        default=NOTHING, name="lastTrafficResetAt", converter=msgspex.From[str | datetime | None]
    )


class DebugSrrMatcherRequestDtoResponseRulesSettings(msgspex.Model, kw_only=True):
    """{"markdownDescription":"Settings for the **response rules** config. Optional."}"""

    disable_subscription_access_by_path: msgspex.Option[bool] = msgspex.field(
        default=..., name="disableSubscriptionAccessByPath", converter=msgspex.From[bool | None]
    )
    """{"markdownDescription":"Usually, a user's subscription may also be available via additional paths such as **/json**, **/stash**, or **/mihomo**. If this flag is set to **true**, access via these additional paths will be disabled."}"""


class DebugSrrMatcherRequestDtoResponseRulesRulesConditions(msgspex.Model, kw_only=True):
    r"""{"markdownDescription":"Condition to check against the **headerName**.","defaultSnippets":[{"label":"Examples: Check if header contains \"text/html\"","markdownDescription":"Condition to check if **headerName** contains \"text/html\"","body":{"headerName":"accept","operator":"CONTAINS","value":"text/html","caseSensitive":true}}]}"""

    header_name: typing.Annotated[str, msgspec.Meta(pattern="^[!#$%&'*+\\-.0-9A-Z^_`a-z|~]+$")] = msgspex.field(name="headerName")
    """{"markdownDescription":"**Name** of the HTTP header to check. Must comply with RFC 7230."}"""

    operator: DebugSrrMatcherRequestDtoResponseRulesRulesConditionsOperator
    """{"errorMessage":"Invalid operator. Please select a valid operator.","markdownDescription":"Operator to use for comparing the `headerName` with `value`.","markdownEnumDescriptions":["Performs an exact, comparison between the header value and specified string. `string === value`","Ensures the header value does not exactly match the specified string. `string !== value`","Checks if the header value contains the specified string as a substring. `string.includes()`","Verifies the header value does not contain the specified string as a substring. `!string.includes()`","Validates that the header value begins with the specified string. `string.startsWith()`","Validates that the header value does not begin with the specified string. `!string.startsWith()`","Confirms the header value ends with the specified string. `string.endsWith()`","Confirms the header value does not end with the specified string. `!string.endsWith()`","Evaluates if the header value matches the specified regular expression pattern. `regex.test()`","Evaluates if the header value does not match the specified regular expression pattern. `!regex.test()`"]}"""

    value: typing.Annotated[str, msgspec.Meta(min_length=1, max_length=255)]
    """{"markdownDescription":"**Value** to check against the **headerName**."}"""

    case_sensitive: bool = msgspex.field(name="caseSensitive")
    """{"markdownDescription":"Whether the value is **case sensitive**. \n\n - `true`: the value will be compared as is. \n\n - `false`: the value will be lowercased **before** comparison."}"""


class DebugSrrMatcherRequestDtoResponseRulesRulesResponseModificationsHeaders(msgspex.Model, kw_only=True):
    """{"markdownDescription":"**Key** and **value** of the response header will be added to the response."}"""

    key: typing.Annotated[str, msgspec.Meta(pattern="^[!#$%&'*+\\-.0-9A-Z^_`a-z|~]+$")]
    """{"markdownDescription":"Key of the response header. Must comply with RFC 7230."}"""

    value: typing.Annotated[str, msgspec.Meta(min_length=1)]
    """{"markdownDescription":"Value of the response header. "}"""


class DebugSrrMatcherRequestDtoResponseRulesRulesResponseModifications(msgspex.Model, kw_only=True):
    """{"examples":[{"headers":[{"key":"X-Custom-Header","value":"CustomValue"}]}],"markdownDescription":"Response modifications to be applied when the rule is matched. Optional."}"""

    headers: msgspex.Option[list[DebugSrrMatcherRequestDtoResponseRulesRulesResponseModificationsHeaders]] = msgspex.field(
        default=..., converter=msgspex.From["list[DebugSrrMatcherRequestDtoResponseRulesRulesResponseModificationsHeaders] | None"]
    )
    """{"defaultSnippets":[{"label":"Examples: Add custom header","markdownDescription":"Add a custom header to the response","body":[{"key":"X-Custom-Header","value":"CustomValue"}]}],"markdownDescription":"Array of headers to be added when the rule is matched."}"""

    apply_headers_to_end: msgspex.Option[bool] = msgspex.field(default=..., name="applyHeadersToEnd", converter=msgspex.From[bool | None])
    """{"markdownDescription":"By default, headers are added when forming the response. In some cases, headers set in SRR may be overridden by headers from other parts of the system. If you set this flag to **true**, headers from SRR will be added at the very end, just before the response is sent. In this case, SRR headers may override headers from other sections."}"""

    subscription_template: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=1)]] = msgspex.field(
        default=..., name="subscriptionTemplate", converter=msgspex.From[str | None]
    )
    """{"markdownDescription":"Override the subscription template with the given name. If not provided, the default subscription template will be used. If the template name is not found, the default subscription template for this type will be used. **This modification have higher priority than settings from External Squads.**"}"""

    ignore_host_xray_json_template: msgspex.Option[bool] = msgspex.field(default=..., name="ignoreHostXrayJsonTemplate", converter=msgspex.From[bool | None])
    """{"markdownDescription":"Each Host may have its own Xray Json Template. If you set this flag to **true**, the Xray Json Template defined by the SRR will be used. **The Host's Xray Json Template will be ignored.**"}"""

    ignore_serve_json_at_base_subscription: msgspex.Option[bool] = msgspex.field(
        default=..., name="ignoreServeJsonAtBaseSubscription", converter=msgspex.From[bool | None]
    )
    """{"markdownDescription":"If you set this flag to **true**, the **Serve JSON at Base Subscription** setting will be ignored (set to **false**)."}"""


class DebugSrrMatcherRequestDtoResponseRulesRules(msgspex.Model, kw_only=True):
    r"""{"defaultSnippets":[{"label":"Examples: Blank rule","markdownDescription":"Simple blank rule with no conditions or modifications.\n```json\n{\n  \"name\": \"Blank rule\",\n  \"description\": \"Blank rule\",\n  \"operator\": \"AND\",\n  \"enabled\": true,\n  \"conditions\": [],\n  \"responseType\": \"BLOCK\",\n  \"responseModifications\": {\n    \"headers\": []\n  }\n}\n```","body":{"name":"Blank rule","description":"Blank rule","operator":"AND","enabled":true,"conditions":[],"responseType":"BLOCK","responseModifications":{"headers":[]}}},{"label":"Examples: Block Legacy Clients","markdownDescription":"Block requests from legacy clients\n```json\n{\n  \"name\": \"Block Legacy Clients\",\n  \"description\": \"Block requests from legacy clients\",\n  \"enabled\": true,\n  \"operator\": \"OR\",\n  \"conditions\": [\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"Hiddify\",\n      \"caseSensitive\": true\n    },\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"FoxRay\",\n      \"caseSensitive\": true\n    }\n  ],\n  \"responseType\": \"BLOCK\"\n}\n```","body":{"name":"Block Legacy Clients","description":"Block requests from legacy clients","enabled":true,"operator":"OR","conditions":[{"headerName":"user-agent","operator":"CONTAINS","value":"Hiddify","caseSensitive":true},{"headerName":"user-agent","operator":"CONTAINS","value":"FoxRay","caseSensitive":true}],"responseType":"BLOCK"}}],"title":"Response Rule","markdownDescription":"Response rule configuration.\n\n**Fields:**\n- **name**: Name of the response rule.\n- **description**: Description of the response rule. Optional.\n- **enabled**: Control whether the response rule is enabled or disabled. \n\n - `true` the rule will be applied. \n\n - `false` the rule will be always ignored.\n- **operator**: Operator to use for combining conditions in the rule.\n- **conditions**: Array of conditions to check against the request headers. Conditions are applied with **operator**. If conditions are empty, the rule will be matched.\n- **responseType**: Type of the response. Determines the type of **response** to be returned when the rule is matched.\n- **responseModifications**: Response modifications to be applied when the rule is matched. Optional.\n\n**Example:**\n```json\n{\n  \"name\": \"Block Legacy Clients\",\n  \"description\": \"Block requests from legacy clients\",\n  \"enabled\": true,\n  \"operator\": \"OR\",\n  \"conditions\": [\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"Hiddify\",\n      \"caseSensitive\": true\n    },\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"FoxRay\",\n      \"caseSensitive\": true\n    }\n  ],\n  \"responseType\": \"BLOCK\"\n}\n```"}"""

    name: typing.Annotated[str, msgspec.Meta(min_length=1, max_length=50)]
    """{"markdownDescription":"Name of the response rule."}"""

    enabled: bool
    """{"markdownDescription":"Control whether the response rule is enabled or disabled. \n\n - `true` the rule will be applied. \n\n - `false` the rule will be always ignored."}"""

    operator: DebugSrrMatcherRequestDtoResponseRulesRulesOperator
    """{"markdownDescription":"Operator to use for combining conditions in the rule."}"""

    conditions: list[DebugSrrMatcherRequestDtoResponseRulesRulesConditions]
    """{"markdownDescription":"Array of conditions to check against the request headers. Conditions are applied with **operator**. If conditions are empty, the rule will be matched."}"""

    response_type: DebugSrrMatcherRequestDtoResponseRulesRulesResponseType = msgspex.field(name="responseType")
    """{"errorMessage":"Invalid response type. Please select a valid response type.","markdownDescription":"Type of the response. Determines the type of **response** to be returned when the rule is matched.","markdownEnumDescriptions":["Return **subscription** in XRAY-JSON format. (Using `Xray Json` template)","Return **subscription** in BASE64 encoded string. Compatible with most client application with Xray core.","Return **subscription** in Mihomo format. (Using `Mihomo` template)","Return **subscription** in Stash format. (Using `Stash` template)","Return **subscription** in Clash format. (Using `Clash` template) Useful for client application that use Legacy Clash core.","Return **subscription** in Singbox format. (Using `Singbox` template) Format which is used by Singbox client application.","Return **subscription** as browser format. The same as on `/info` route.","**Drop** request and return `403` status code.","**Drop** request and return `404` status code.","**Drop** request and return `451` status code.","**Drop** the socket connection."]}"""

    description: msgspex.Option[typing.Annotated[str, msgspec.Meta(min_length=1, max_length=250)]] = msgspex.field(
        default=..., converter=msgspex.From[str | None]
    )
    """{"markdownDescription":"Description of the response rule. Optional."}"""

    response_modifications: msgspex.Option[DebugSrrMatcherRequestDtoResponseRulesRulesResponseModifications] = msgspex.field(
        default=..., name="responseModifications", converter=msgspex.From["DebugSrrMatcherRequestDtoResponseRulesRulesResponseModifications | None"]
    )
    """{"examples":[{"headers":[{"key":"X-Custom-Header","value":"CustomValue"}]}],"markdownDescription":"Response modifications to be applied when the rule is matched. Optional."}"""


class DebugSrrMatcherRequestDtoResponseRules(msgspex.Model, kw_only=True):
    version: DebugSrrMatcherRequestDtoResponseRulesVersion
    """{"title":"Response Rules Config Version","markdownDescription":"Version of the **response rules** config. Currently supported version is **1**."}"""

    rules: list[DebugSrrMatcherRequestDtoResponseRulesRules]
    """{"title":"Response Rules","markdownDescription":"Array of **response rules**. Rules are evaluated in order and the first rule that matches is applied. If no rule matches, request will be blocked by default.\n\n**Example:**\n```json\n[\n  {\n    \"name\": \"Blank rule\",\n    \"description\": \"Blank rule\",\n    \"operator\": \"AND\",\n    \"enabled\": true,\n    \"conditions\": [],\n    \"responseType\": \"BLOCK\",\n    \"responseModifications\": {\n      \"headers\": []\n    }\n  }\n]\n```","defaultSnippets":[]}"""

    settings: msgspex.Option[DebugSrrMatcherRequestDtoResponseRulesSettings] = msgspex.field(
        default=..., converter=msgspex.From["DebugSrrMatcherRequestDtoResponseRulesSettings | None"]
    )
    """{"markdownDescription":"Settings for the **response rules** config. Optional."}"""


class DebugSrrMatcherResponseDtoResponse(msgspex.Model, kw_only=True):
    matched: bool
    response_type: DebugSrrMatcherResponseDtoResponseResponseType = msgspex.field(name="responseType")
    input_headers: dict[str, str] = msgspex.field(name="inputHeaders")
    output_headers: dict[str, str] = msgspex.field(name="outputHeaders")
    matched_rule: msgspex.NullableOption[DebugSrrMatcherRequestDtoResponseRulesRules] = msgspex.field(default=NOTHING, name="matchedRule")
    """{"defaultSnippets":[{"label":"Examples: Blank rule","markdownDescription":"Simple blank rule with no conditions or modifications.\n```json\n{\n  \"name\": \"Blank rule\",\n  \"description\": \"Blank rule\",\n  \"operator\": \"AND\",\n  \"enabled\": true,\n  \"conditions\": [],\n  \"responseType\": \"BLOCK\",\n  \"responseModifications\": {\n    \"headers\": []\n  }\n}\n```","body":{"name":"Blank rule","description":"Blank rule","operator":"AND","enabled":true,"conditions":[],"responseType":"BLOCK","responseModifications":{"headers":[]}}},{"label":"Examples: Block Legacy Clients","markdownDescription":"Block requests from legacy clients\n```json\n{\n  \"name\": \"Block Legacy Clients\",\n  \"description\": \"Block requests from legacy clients\",\n  \"enabled\": true,\n  \"operator\": \"OR\",\n  \"conditions\": [\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"Hiddify\",\n      \"caseSensitive\": true\n    },\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"FoxRay\",\n      \"caseSensitive\": true\n    }\n  ],\n  \"responseType\": \"BLOCK\"\n}\n```","body":{"name":"Block Legacy Clients","description":"Block requests from legacy clients","enabled":true,"operator":"OR","conditions":[{"headerName":"user-agent","operator":"CONTAINS","value":"Hiddify","caseSensitive":true},{"headerName":"user-agent","operator":"CONTAINS","value":"FoxRay","caseSensitive":true}],"responseType":"BLOCK"}}],"title":"Response Rule","markdownDescription":"Response rule configuration.\n\n**Fields:**\n- **name**: Name of the response rule.\n- **description**: Description of the response rule. Optional.\n- **enabled**: Control whether the response rule is enabled or disabled. \n\n - `true` the rule will be applied. \n\n - `false` the rule will be always ignored.\n- **operator**: Operator to use for combining conditions in the rule.\n- **conditions**: Array of conditions to check against the request headers. Conditions are applied with **operator**. If conditions are empty, the rule will be matched.\n- **responseType**: Type of the response. Determines the type of **response** to be returned when the rule is matched.\n- **responseModifications**: Response modifications to be applied when the rule is matched. Optional.\n\n**Example:**\n```json\n{\n  \"name\": \"Block Legacy Clients\",\n  \"description\": \"Block requests from legacy clients\",\n  \"enabled\": true,\n  \"operator\": \"OR\",\n  \"conditions\": [\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"Hiddify\",\n      \"caseSensitive\": true\n    },\n    {\n      \"headerName\": \"user-agent\",\n      \"operator\": \"CONTAINS\",\n      \"value\": \"FoxRay\",\n      \"caseSensitive\": true\n    }\n  ],\n  \"responseType\": \"BLOCK\"\n}\n```"}"""


class DeleteConfigProfileResponseDtoResponse(msgspex.Model, kw_only=True):
    is_deleted: bool = msgspex.field(name="isDeleted")


class DeletePasskeyResponseDtoResponsePasskeys(msgspex.Model, kw_only=True):
    id: str
    name: str
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    """Created date. Format: 2025-01-17T15:38:45.065Z"""

    last_used_at: msgspex.isodatetime = msgspex.field(name="lastUsedAt", converter=msgspex.From[str | datetime])
    """Last used date. Format: 2025-01-17T15:38:45.065Z"""


class DeletePasskeyResponseDtoResponse(msgspex.Model, kw_only=True):
    passkeys: list[DeletePasskeyResponseDtoResponsePasskeys]


class DropConnectionsRequestDtoDropBy(msgspex.Model, kw_only=True):
    """Drop by user UUIDs"""

    by: DropConnectionsRequestDtoDropByBy
    user_uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1)] = msgspex.field(name="userUuids", converter=msgspex.From[list[str | UUID]])


class DropConnectionsRequestDtoDropBy2(msgspex.Model, kw_only=True):
    """Drop by IP addresses"""

    by: DropConnectionsRequestDtoDropBy2By
    ip_addresses: typing.Annotated[list[str], msgspec.Meta(min_length=1)] = msgspex.field(name="ipAddresses")


class DropConnectionsRequestDtoTargetNodes(msgspex.Model, kw_only=True):
    """Target all connected nodes"""

    target: DropConnectionsRequestDtoTargetNodesTarget


class DropConnectionsRequestDtoTargetNodes2(msgspex.Model, kw_only=True):
    """Target specific nodes"""

    target: DropConnectionsRequestDtoTargetNodes2Target
    node_uuids: typing.Annotated[list[UUID], msgspec.Meta(min_length=1)] = msgspex.field(name="nodeUuids", converter=msgspex.From[list[str | UUID]])


class EncryptHappCryptoLinkResponseDtoResponse(msgspex.Model, kw_only=True):
    encrypted_link: str = msgspex.field(name="encryptedLink")


class FetchIpsResponseDtoResponse(msgspex.Model, kw_only=True):
    job_id: str = msgspex.field(name="jobId")


class FetchIpsResultResponseDtoResponseProgress(msgspex.Model, kw_only=True):
    total: int
    completed: int
    percent: int


class FetchIpsResultResponseDtoResponseResultNodes(FetchIpsResultResponseDtoResponseResultNodesBase, kw_only=True):
    ips: list[str]


class FetchIpsResultResponseDtoResponseResult(msgspex.Model, kw_only=True):
    success: bool
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])
    user_id: str = msgspex.field(name="userId")
    nodes: list[FetchIpsResultResponseDtoResponseResultNodes]


class FetchIpsResultResponseDtoResponse(msgspex.Model, kw_only=True):
    is_completed: bool = msgspex.field(name="isCompleted")
    is_failed: bool = msgspex.field(name="isFailed")
    progress: FetchIpsResultResponseDtoResponseProgress
    result: msgspex.NullableOption[FetchIpsResultResponseDtoResponseResult] = msgspex.field(default=NOTHING)


class FindAllApiTokensResponseDtoResponseApiKeys(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    token: str
    token_name: str = msgspex.field(name="tokenName")
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])


class FindAllApiTokensResponseDtoResponseDocs(msgspex.Model, kw_only=True):
    is_docs_enabled: bool = msgspex.field(name="isDocsEnabled")
    scalar_path: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="scalarPath")
    swagger_path: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="swaggerPath")


class FindAllApiTokensResponseDtoResponse(msgspex.Model, kw_only=True):
    api_keys: list[FindAllApiTokensResponseDtoResponseApiKeys] = msgspex.field(name="apiKeys")
    docs: FindAllApiTokensResponseDtoResponseDocs


class GenerateX25519ResponseDtoResponseKeypairs(msgspex.Model, kw_only=True):
    public_key: str = msgspex.field(name="publicKey")
    private_key: str = msgspex.field(name="privateKey")


class GenerateX25519ResponseDtoResponse(msgspex.Model, kw_only=True):
    keypairs: list[GenerateX25519ResponseDtoResponseKeypairs]


class GetAllHostTagsResponseDtoResponse(msgspex.Model, kw_only=True):
    tags: list[str]


class GetAllInboundsResponseDtoResponseInbounds(ResponseDtoResponseInboundsBase, kw_only=True):
    active_squads: list[UUID] = msgspex.field(name="activeSquads", converter=msgspex.From[list[str | UUID]])


class GetAllInboundsResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    inbounds: list[GetAllInboundsResponseDtoResponseInbounds]


class GetAllSubscriptionsResponseDtoResponseSubscriptionsUser(msgspex.Model, kw_only=True):
    short_uuid: str = msgspex.field(name="shortUuid")
    days_left: int = msgspex.field(name="daysLeft")
    traffic_used: str = msgspex.field(name="trafficUsed")
    traffic_limit: str = msgspex.field(name="trafficLimit")
    lifetime_traffic_used: str = msgspex.field(name="lifetimeTrafficUsed")
    traffic_used_bytes: str = msgspex.field(name="trafficUsedBytes")
    traffic_limit_bytes: str = msgspex.field(name="trafficLimitBytes")
    lifetime_traffic_used_bytes: str = msgspex.field(name="lifetimeTrafficUsedBytes")
    username: str
    expires_at: msgspex.isodatetime = msgspex.field(name="expiresAt", converter=msgspex.From[str | datetime])
    is_active: bool = msgspex.field(name="isActive")
    user_status: Status = msgspex.field(name="userStatus")
    traffic_limit_strategy: GetAllSubscriptionsResponseDtoResponseSubscriptionsUserTrafficLimitStrategy = msgspex.field(name="trafficLimitStrategy")


class GetAllSubscriptionsResponseDtoResponseSubscriptions(msgspex.Model, kw_only=True):
    is_found: bool = msgspex.field(name="isFound")
    user: GetAllSubscriptionsResponseDtoResponseSubscriptionsUser
    links: list[str]
    ss_conf_links: dict[str, str] = msgspex.field(name="ssConfLinks")
    subscription_url: str = msgspex.field(name="subscriptionUrl")


class GetAllSubscriptionsResponseDtoResponse(msgspex.Model, kw_only=True):
    subscriptions: list[GetAllSubscriptionsResponseDtoResponseSubscriptions]
    total: int


class GetAllUsersResponseDtoResponse(msgspex.Model, kw_only=True):
    users: list[CreateUserResponseDtoResponse]
    total: int


class GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays(msgspex.Model, kw_only=True):
    current: str
    previous: str
    difference: str


class GetBandwidthStatsResponseDtoResponse(msgspex.Model, kw_only=True):
    bandwidth_last_two_days: GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays = msgspex.field(name="bandwidthLastTwoDays")
    bandwidth_last_seven_days: GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays = msgspex.field(name="bandwidthLastSevenDays")
    bandwidth_last30_days: GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays = msgspex.field(name="bandwidthLast30Days")
    bandwidth_calendar_month: GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays = msgspex.field(name="bandwidthCalendarMonth")
    bandwidth_current_year: GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays = msgspex.field(name="bandwidthCurrentYear")


class GetConfigProfilesResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    config_profiles: list[CreateConfigProfileResponseDtoResponse] = msgspex.field(name="configProfiles")


class GetConnectionKeysByUuidResponseDtoResponse(msgspex.Model, kw_only=True):
    enabled_keys: list[str] = msgspex.field(name="enabledKeys")
    hidden_keys: list[str] = msgspex.field(name="hiddenKeys")
    disabled_keys: list[str] = msgspex.field(name="disabledKeys")


class GetExternalSquadsResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    external_squads: list[CreateExternalSquadResponseDtoResponse] = msgspex.field(name="externalSquads")


class GetHwidDevicesStatsResponseDtoResponseByPlatform(msgspex.Model, kw_only=True):
    platform: str
    count: int


class GetHwidDevicesStatsResponseDtoResponseByApp(msgspex.Model, kw_only=True):
    app: str
    count: int


class GetHwidDevicesStatsResponseDtoResponseStats(msgspex.Model, kw_only=True):
    total_unique_devices: int = msgspex.field(name="totalUniqueDevices")
    total_hwid_devices: int = msgspex.field(name="totalHwidDevices")
    average_hwid_devices_per_user: int = msgspex.field(name="averageHwidDevicesPerUser")


class GetHwidDevicesStatsResponseDtoResponse(msgspex.Model, kw_only=True):
    by_platform: list[GetHwidDevicesStatsResponseDtoResponseByPlatform] = msgspex.field(name="byPlatform")
    by_app: list[GetHwidDevicesStatsResponseDtoResponseByApp] = msgspex.field(name="byApp")
    stats: GetHwidDevicesStatsResponseDtoResponseStats


class GetInfraProvidersResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    providers: list[CreateInfraProviderResponseDtoResponse]


class GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodes(NodesBase, kw_only=True):
    active_inbounds: list[str] = msgspex.field(name="activeInbounds")


class GetInternalSquadAccessibleNodesResponseDtoResponse(msgspex.Model, kw_only=True):
    squad_uuid: UUID = msgspex.field(name="squadUuid", converter=msgspex.From[str | UUID])
    accessible_nodes: list[GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodes] = msgspex.field(name="accessibleNodes")


class GetInternalSquadsResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    internal_squads: list[CreateInternalSquadResponseDtoResponse] = msgspex.field(name="internalSquads")


class GetLegacyStatsNodesUsersUsageResponseDtoResponse(msgspex.Model, kw_only=True):
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])
    username: str
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    total: int
    date: date = msgspex.field(converter=msgspex.From[str | date])


class GetLegacyStatsUserUsageResponseDtoResponse(msgspex.Model, kw_only=True):
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])
    node_uuid: UUID = msgspex.field(name="nodeUuid", converter=msgspex.From[str | UUID])
    node_name: str = msgspex.field(name="nodeName")
    country_code: str = msgspex.field(name="countryCode")
    total: int
    date: date = msgspex.field(converter=msgspex.From[str | date])


class GetMetadataResponseDtoResponseBuild(msgspex.Model, kw_only=True):
    time: str
    number: str


class GetMetadataResponseDtoResponseGitBackend(msgspex.Model, kw_only=True):
    commit_sha: str = msgspex.field(name="commitSha")
    branch: str
    commit_url: str = msgspex.field(name="commitUrl")


class GetMetadataResponseDtoResponseGitFrontend(msgspex.Model, kw_only=True):
    commit_sha: str = msgspex.field(name="commitSha")
    commit_url: str = msgspex.field(name="commitUrl")


class GetMetadataResponseDtoResponseGit(msgspex.Model, kw_only=True):
    backend: GetMetadataResponseDtoResponseGitBackend
    frontend: GetMetadataResponseDtoResponseGitFrontend


class GetMetadataResponseDtoResponse(msgspex.Model, kw_only=True):
    version: str
    build: GetMetadataResponseDtoResponseBuild
    git: GetMetadataResponseDtoResponseGit


class GetNodesStatisticsResponseDtoResponseLastSevenDays(msgspex.Model, kw_only=True):
    node_name: str = msgspex.field(name="nodeName")
    date: date = msgspex.field(converter=msgspex.From[str | date])
    total_bytes: str = msgspex.field(name="totalBytes")


class GetNodesStatisticsResponseDtoResponse(msgspex.Model, kw_only=True):
    last_seven_days: list[GetNodesStatisticsResponseDtoResponseLastSevenDays] = msgspex.field(name="lastSevenDays")


class GetPubKeyResponseDtoResponse(msgspex.Model, kw_only=True):
    pub_key: str = msgspex.field(name="pubKey")


class GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo(msgspex.Model, kw_only=True):
    days_left: int = msgspex.field(name="daysLeft")
    traffic_limit: str = msgspex.field(name="trafficLimit")
    traffic_used: str = msgspex.field(name="trafficUsed")
    lifetime_traffic_used: str = msgspex.field(name="lifetimeTrafficUsed")
    is_hwid_limited: bool = msgspex.field(name="isHwidLimited")


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsPassword(msgspex.Model, kw_only=True):
    ss_password: str = msgspex.field(name="ssPassword")
    trojan_password: str = msgspex.field(name="trojanPassword")
    vless_password: str = msgspex.field(name="vlessPassword")


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsRawSettings(msgspex.Model, kw_only=True):
    header_type: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="headerType", converter=msgspex.From[str | None])
    request: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(default=NOTHING, converter=msgspex.From[dict[str, typing.Any] | None])


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsAdditionalParams(msgspex.Model, kw_only=True):
    mode: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    heartbeat_period: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="heartbeatPeriod", converter=msgspex.From[int | None])


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptionsSs(msgspex.Model, kw_only=True):
    method: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptions(msgspex.Model, kw_only=True):
    ss: msgspex.NullableOption[GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptionsSs] = msgspex.field(
        default=NOTHING, converter=msgspex.From["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptionsSs | None"]
    )


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsDbData(msgspex.Model, kw_only=True):
    inbound_tag: str = msgspex.field(name="inboundTag")
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    is_disabled: bool = msgspex.field(name="isDisabled")
    view_position: int = msgspex.field(name="viewPosition")
    remark: str
    is_hidden: bool = msgspex.field(name="isHidden")
    raw_inbound: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(default=NOTHING, name="rawInbound")
    config_profile_uuid: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="configProfileUuid")
    config_profile_inbound_uuid: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="configProfileInboundUuid")
    tag: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    vless_route_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="vlessRouteId")


class GetRawSubscriptionByShortUuidResponseDtoResponseRawHosts(msgspex.Model, kw_only=True):
    password: GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsPassword
    address: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    alpn: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    fingerprint: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    host: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    network: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    path: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    public_key: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="publicKey", converter=msgspex.From[str | None])
    port: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, converter=msgspex.From[int | None])
    protocol: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    remark: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    short_id: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="shortId", converter=msgspex.From[str | None])
    sni: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    spider_x: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="spiderX", converter=msgspex.From[str | None])
    tls: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    raw_settings: msgspex.NullableOption[GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsRawSettings] = msgspex.field(
        default=NOTHING, name="rawSettings", converter=msgspex.From["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsRawSettings | None"]
    )
    additional_params: msgspex.NullableOption[GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsAdditionalParams] = msgspex.field(
        default=NOTHING, name="additionalParams", converter=msgspex.From["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsAdditionalParams | None"]
    )
    x_http_extra_params: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(
        default=NOTHING, name="xHttpExtraParams", converter=msgspex.From[dict[str, typing.Any] | None]
    )
    mux_params: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(
        default=NOTHING, name="muxParams", converter=msgspex.From[dict[str, typing.Any] | None]
    )
    sockopt_params: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(
        default=NOTHING, name="sockoptParams", converter=msgspex.From[dict[str, typing.Any] | None]
    )
    server_description: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="serverDescription", converter=msgspex.From[str | None])
    flow: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    allow_insecure: msgspex.NullableOption[bool] = msgspex.field(default=NOTHING, name="allowInsecure", converter=msgspex.From[bool | None])
    shuffle_host: msgspex.NullableOption[bool] = msgspex.field(default=NOTHING, name="shuffleHost", converter=msgspex.From[bool | None])
    mihomo_x25519: msgspex.NullableOption[bool] = msgspex.field(default=NOTHING, name="mihomoX25519", converter=msgspex.From[bool | None])
    mldsa65_verify: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="mldsa65Verify", converter=msgspex.From[str | None])
    encryption: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, converter=msgspex.From[str | None])
    protocol_options: msgspex.NullableOption[GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptions] = msgspex.field(
        default=NOTHING, name="protocolOptions", converter=msgspex.From["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptions | None"]
    )
    db_data: msgspex.Option[GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsDbData] = msgspex.field(
        default=..., name="dbData", converter=msgspex.From["GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsDbData | None"]
    )
    xray_json_template: msgspex.NullableOption[dict[str, typing.Any]] = msgspex.field(
        default=NOTHING, name="xrayJsonTemplate", converter=msgspex.From[dict[str, typing.Any] | None]
    )


class GetRawSubscriptionByShortUuidResponseDtoResponse(msgspex.Model, kw_only=True):
    user: CreateUserResponseDtoResponse
    converted_user_info: GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo = msgspex.field(name="convertedUserInfo")
    headers: dict[str, str]
    raw_hosts: list[GetRawSubscriptionByShortUuidResponseDtoResponseRawHosts] = msgspex.field(name="rawHosts")


class GetRemnawaveHealthResponseDtoResponsePm2Stats(msgspex.Model, kw_only=True):
    name: str
    memory: str
    cpu: str


class GetRemnawaveHealthResponseDtoResponse(msgspex.Model, kw_only=True):
    pm2_stats: list[GetRemnawaveHealthResponseDtoResponsePm2Stats] = msgspex.field(name="pm2Stats")


class GetRemnawaveSettingsResponseDtoResponsePasskeySettings(msgspex.Model, kw_only=True):
    enabled: bool
    rp_id: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="rpId")
    origin: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)


class GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub(RemnawaveSettingsResponseDtoResponseOauth2SettingsBase, kw_only=True):
    allowed_emails: list[str] = msgspex.field(name="allowedEmails")


class GetRemnawaveSettingsResponseDtoResponseOauth2SettingsPocketid(RemnawaveSettingsResponseDtoResponseOauth2SettingsBase, kw_only=True):
    allowed_emails: list[str] = msgspex.field(name="allowedEmails")
    plain_domain: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="plainDomain")


class GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak(msgspex.Model, kw_only=True):
    enabled: bool
    allowed_emails: list[str] = msgspex.field(name="allowedEmails")
    realm: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    client_id: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="clientId")
    client_secret: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="clientSecret")
    frontend_domain: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="frontendDomain")
    keycloak_domain: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="keycloakDomain")


class GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric(RemnawaveSettingsResponseDtoResponseOauth2SettingsBase, kw_only=True):
    with_pkce: bool = msgspex.field(name="withPkce")
    allowed_emails: list[str] = msgspex.field(name="allowedEmails")
    authorization_url: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="authorizationUrl")
    token_url: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="tokenUrl")
    frontend_domain: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="frontendDomain")


class GetRemnawaveSettingsResponseDtoResponseOauth2Settings(msgspex.Model, kw_only=True):
    github: GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub
    pocketid: GetRemnawaveSettingsResponseDtoResponseOauth2SettingsPocketid
    yandex: GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub
    keycloak: msgspex.Option[GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak] = msgspex.field(
        default=..., converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak | None"]
    )
    generic: msgspex.Option[GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric] = msgspex.field(
        default=..., converter=msgspex.From["GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric | None"]
    )


class GetRemnawaveSettingsResponseDtoResponseTgAuthSettings(msgspex.Model, kw_only=True):
    enabled: bool
    admin_ids: list[str] = msgspex.field(name="adminIds")
    bot_token: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="botToken")


class GetRemnawaveSettingsResponseDtoResponsePasswordSettings(msgspex.Model, kw_only=True):
    enabled: bool


class GetRemnawaveSettingsResponseDtoResponseBrandingSettings(msgspex.Model, kw_only=True):
    title: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    logo_url: msgspex.NullableOption[msgspex.URI] = msgspex.field(default=NOTHING, name="logoUrl", converter=msgspex.From[str | msgspex.URI | None])


class GetRemnawaveSettingsResponseDtoResponse(msgspex.Model, kw_only=True):
    passkey_settings: msgspex.NullableOption[GetRemnawaveSettingsResponseDtoResponsePasskeySettings] = msgspex.field(default=NOTHING, name="passkeySettings")
    oauth2_settings: msgspex.NullableOption[GetRemnawaveSettingsResponseDtoResponseOauth2Settings] = msgspex.field(default=NOTHING, name="oauth2Settings")
    tg_auth_settings: msgspex.NullableOption[GetRemnawaveSettingsResponseDtoResponseTgAuthSettings] = msgspex.field(default=NOTHING, name="tgAuthSettings")
    password_settings: msgspex.NullableOption[GetRemnawaveSettingsResponseDtoResponsePasswordSettings] = msgspex.field(default=NOTHING, name="passwordSettings")
    branding_settings: msgspex.NullableOption[GetRemnawaveSettingsResponseDtoResponseBrandingSettings] = msgspex.field(default=NOTHING, name="brandingSettings")


class GetStatsNodeUsersUsageResponseDtoResponseTopUsers(msgspex.Model, kw_only=True):
    color: str
    username: str
    total: int


class GetStatsNodeUsersUsageResponseDtoResponse(UsageBase, kw_only=True):
    top_users: list[GetStatsNodeUsersUsageResponseDtoResponseTopUsers] = msgspex.field(name="topUsers")


class GetStatsNodesRealtimeUsageResponseDtoResponse(FetchIpsResultResponseDtoResponseResultNodesBase, kw_only=True):
    download_bytes: int = msgspex.field(name="downloadBytes")
    upload_bytes: int = msgspex.field(name="uploadBytes")
    total_bytes: int = msgspex.field(name="totalBytes")
    download_speed_bps: int = msgspex.field(name="downloadSpeedBps")
    upload_speed_bps: int = msgspex.field(name="uploadSpeedBps")
    total_speed_bps: int = msgspex.field(name="totalSpeedBps")


class GetStatsNodesUsageResponseDtoResponseTopNodes(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    color: str
    name: str
    country_code: str = msgspex.field(name="countryCode")
    total: int


class GetStatsNodesUsageResponseDtoResponseSeries(CreateConfigProfileResponseDtoResponseNodesBase, kw_only=True):
    color: str
    country_code: str = msgspex.field(name="countryCode")
    total: int
    data: list[int]


class GetStatsNodesUsageResponseDtoResponse(UsageBase, kw_only=True):
    top_nodes: list[GetStatsNodesUsageResponseDtoResponseTopNodes] = msgspex.field(name="topNodes")
    series: list[GetStatsNodesUsageResponseDtoResponseSeries]


class GetStatsResponseDtoResponseCpu(msgspex.Model, kw_only=True):
    cores: int
    physical_cores: int = msgspex.field(name="physicalCores")


class GetStatsResponseDtoResponseMemory(msgspex.Model, kw_only=True):
    total: int
    free: int
    used: int
    active: int
    available: int


class GetStatsResponseDtoResponseUsers(msgspex.Model, kw_only=True):
    status_counts: dict[str, int] = msgspex.field(name="statusCounts")
    total_users: int = msgspex.field(name="totalUsers")


class GetStatsResponseDtoResponseOnlineStats(msgspex.Model, kw_only=True):
    last_day: int = msgspex.field(name="lastDay")
    last_week: int = msgspex.field(name="lastWeek")
    never_online: int = msgspex.field(name="neverOnline")
    online_now: int = msgspex.field(name="onlineNow")


class GetStatsResponseDtoResponseNodes(msgspex.Model, kw_only=True):
    total_online: int = msgspex.field(name="totalOnline")
    total_bytes_lifetime: str = msgspex.field(name="totalBytesLifetime")


class GetStatsResponseDtoResponse(msgspex.Model, kw_only=True):
    cpu: GetStatsResponseDtoResponseCpu
    memory: GetStatsResponseDtoResponseMemory
    uptime: int
    timestamp: msgspex.IntTimestampDatetime = msgspex.field(converter=msgspex.From[int | datetime])
    users: GetStatsResponseDtoResponseUsers
    online_stats: GetStatsResponseDtoResponseOnlineStats = msgspex.field(name="onlineStats")
    nodes: GetStatsResponseDtoResponseNodes


class GetStatusResponseDtoResponseAuthenticationTgAuth(msgspex.Model, kw_only=True):
    enabled: bool
    bot_id: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="botId")


class GetStatusResponseDtoResponseAuthenticationOauth2(msgspex.Model, kw_only=True):
    providers: dict[str, bool]


class GetStatusResponseDtoResponseAuthentication(msgspex.Model, kw_only=True):
    passkey: GetRemnawaveSettingsResponseDtoResponsePasswordSettings
    tg_auth: GetStatusResponseDtoResponseAuthenticationTgAuth = msgspex.field(name="tgAuth")
    oauth2: GetStatusResponseDtoResponseAuthenticationOauth2
    password: GetRemnawaveSettingsResponseDtoResponsePasswordSettings


class GetStatusResponseDtoResponseBranding(msgspex.Model, kw_only=True):
    title: msgspex.NullableOption[str] = msgspex.field(default=NOTHING)
    logo_url: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="logoUrl")


class GetStatusResponseDtoResponse(msgspex.Model, kw_only=True):
    is_login_allowed: bool = msgspex.field(name="isLoginAllowed")
    is_register_allowed: bool = msgspex.field(name="isRegisterAllowed")
    branding: GetStatusResponseDtoResponseBranding
    authentication: msgspex.NullableOption[GetStatusResponseDtoResponseAuthentication] = msgspex.field(default=NOTHING)


class GetSubpageConfigByShortUuidResponseDtoResponse(msgspex.Model, kw_only=True):
    webpage_allowed: bool = msgspex.field(name="webpageAllowed")
    subpage_config_uuid: msgspex.NullableOption[UUID] = msgspex.field(default=NOTHING, name="subpageConfigUuid", converter=msgspex.From[str | UUID | None])


class GetSubscriptionPageConfigsResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    configs: list[CreateSubscriptionPageConfigResponseDtoResponse]


class GetSubscriptionRequestHistoryStatsResponseDtoResponseHourlyRequestStats(msgspex.Model, kw_only=True):
    date_time: msgspex.isodatetime = msgspex.field(name="dateTime", converter=msgspex.From[str | datetime])
    request_count: int = msgspex.field(name="requestCount")


class GetSubscriptionRequestHistoryStatsResponseDtoResponse(msgspex.Model, kw_only=True):
    by_parsed_app: list[GetHwidDevicesStatsResponseDtoResponseByApp] = msgspex.field(name="byParsedApp")
    hourly_request_stats: list[GetSubscriptionRequestHistoryStatsResponseDtoResponseHourlyRequestStats] = msgspex.field(name="hourlyRequestStats")


class GetSubscriptionSettingsResponseDtoResponse(msgspex.Model, kw_only=True):
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])
    profile_title: str = msgspex.field(name="profileTitle")
    support_link: str = msgspex.field(name="supportLink")
    profile_update_interval: typing.Annotated[int, msgspec.Meta(ge=1)] = msgspex.field(name="profileUpdateInterval")
    is_profile_webpage_url_enabled: bool = msgspex.field(name="isProfileWebpageUrlEnabled")
    serve_json_at_base_subscription: bool = msgspex.field(name="serveJsonAtBaseSubscription")
    is_show_custom_remarks: bool = msgspex.field(name="isShowCustomRemarks")
    custom_remarks: CreateExternalSquadResponseDtoResponseCustomRemarks = msgspex.field(name="customRemarks")
    randomize_hosts: bool = msgspex.field(name="randomizeHosts")
    created_at: msgspex.isodatetime = msgspex.field(name="createdAt", converter=msgspex.From[str | datetime])
    updated_at: msgspex.isodatetime = msgspex.field(name="updatedAt", converter=msgspex.From[str | datetime])
    happ_announce: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="happAnnounce")
    happ_routing: msgspex.NullableOption[str] = msgspex.field(default=NOTHING, name="happRouting")
    custom_response_headers: msgspex.NullableOption[dict[str, str]] = msgspex.field(default=NOTHING, name="customResponseHeaders")
    response_rules: msgspex.NullableOption[DebugSrrMatcherRequestDtoResponseRules] = msgspex.field(default=NOTHING, name="responseRules")
    hwid_settings: msgspex.NullableOption[CreateExternalSquadResponseDtoResponseHwidSettings] = msgspex.field(default=NOTHING, name="hwidSettings")


class GetTemplatesResponseDtoResponse(msgspex.Model, kw_only=True):
    total: int
    templates: list[CreateSubscriptionTemplateResponseDtoResponse]


class GetUserAccessibleNodesResponseDtoResponseActiveNodesActiveSquads(msgspex.Model, kw_only=True):
    squad_name: str = msgspex.field(name="squadName")
    active_inbounds: list[str] = msgspex.field(name="activeInbounds")


class GetUserAccessibleNodesResponseDtoResponseActiveNodes(NodesBase, kw_only=True):
    active_squads: list[GetUserAccessibleNodesResponseDtoResponseActiveNodesActiveSquads] = msgspex.field(name="activeSquads")


class GetUserAccessibleNodesResponseDtoResponse(msgspex.Model, kw_only=True):
    user_uuid: UUID = msgspex.field(name="userUuid", converter=msgspex.From[str | UUID])
    active_nodes: list[GetUserAccessibleNodesResponseDtoResponseActiveNodes] = msgspex.field(name="activeNodes")


class LoginResponseDtoResponse(msgspex.Model, kw_only=True):
    access_token: str = msgspex.field(name="accessToken")


class OAuth2AuthorizeResponseDtoResponse(msgspex.Model, kw_only=True):
    authorization_url: msgspex.NullableOption[msgspex.URI] = msgspex.field(
        default=NOTHING, name="authorizationUrl", converter=msgspex.From[str | msgspex.URI | None]
    )


class RemnawaveWebhookCrmEventsDtoData(msgspex.Model, kw_only=True):
    provider_name: str = msgspex.field(name="providerName")
    node_name: str = msgspex.field(name="nodeName")
    next_billing_at: msgspex.isodatetime = msgspex.field(name="nextBillingAt", converter=msgspex.From[str | datetime])
    login_url: str = msgspex.field(name="loginUrl")


class RemnawaveWebhookErrorsEventsDtoData(msgspex.Model, kw_only=True):
    description: str


class RemnawaveWebhookServiceEventsDtoDataLoginAttempt(msgspex.Model, kw_only=True):
    username: str
    ip: str
    user_agent: str = msgspex.field(name="userAgent")
    description: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])
    password: msgspex.Option[str] = msgspex.field(default=..., converter=msgspex.From[str | None])


class RemnawaveWebhookServiceEventsDtoDataSubpageConfig(msgspex.Model, kw_only=True):
    action: RemnawaveWebhookServiceEventsDtoDataSubpageConfigAction
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])


class RemnawaveWebhookServiceEventsDtoData(msgspex.Model, kw_only=True):
    login_attempt: msgspex.Option[RemnawaveWebhookServiceEventsDtoDataLoginAttempt] = msgspex.field(
        default=..., name="loginAttempt", converter=msgspex.From["RemnawaveWebhookServiceEventsDtoDataLoginAttempt | None"]
    )
    panel_version: msgspex.Option[str] = msgspex.field(default=..., name="panelVersion", converter=msgspex.From[str | None])
    subpage_config: msgspex.Option[RemnawaveWebhookServiceEventsDtoDataSubpageConfig] = msgspex.field(
        default=..., name="subpageConfig", converter=msgspex.From["RemnawaveWebhookServiceEventsDtoDataSubpageConfig | None"]
    )


class RemnawaveWebhookUserEventsDtoMeta(msgspex.Model, kw_only=True):
    not_connected_after_hours: msgspex.NullableOption[int] = msgspex.field(default=NOTHING, name="notConnectedAfterHours", converter=msgspex.From[int | None])


class RemnawaveWebhookUserHwidDevicesEventsDtoData(msgspex.Model, kw_only=True):
    user: CreateUserResponseDtoResponse
    hwid_user_device: CreateUserHwidDeviceResponseDtoResponseDevices = msgspex.field(name="hwidUserDevice")


class ReorderConfigProfilesRequestDtoItems(msgspex.Model, kw_only=True):
    view_position: int = msgspex.field(name="viewPosition")
    uuid: UUID = msgspex.field(converter=msgspex.From[str | UUID])


class ReorderHostResponseDtoResponse(msgspex.Model, kw_only=True):
    is_updated: bool = msgspex.field(name="isUpdated")


class VerifyPasskeyRegistrationResponseDtoResponse(msgspex.Model, kw_only=True):
    verified: bool


class BadRequestErrorErrors(msgspex.Model, kw_only=True):
    validation: str
    code: str
    message: str
    path: list[str]


__all__ = (
    "AddUsersToExternalSquadResponseDtoResponse",
    "BadRequestErrorErrors",
    "BulkAllExtendExpirationDateRequestDto",
    "BulkAllUpdateUsersRequestDto",
    "BulkDeleteHostsRequestDto",
    "BulkDeleteHostsResponseDtoResponse",
    "BulkDeleteHostsResponseDtoResponseInbound",
    "BulkDeleteUsersByStatusRequestDto",
    "BulkDeleteUsersByStatusResponseDtoResponse",
    "BulkDeleteUsersRequestDto",
    "BulkDisableHostsRequestDto",
    "BulkEnableHostsRequestDto",
    "BulkExtendExpirationDateRequestDto",
    "BulkNodesActionsRequestDto",
    "BulkResetTrafficUsersRequestDto",
    "BulkRevokeUsersSubscriptionRequestDto",
    "BulkUpdateUsersRequestDto",
    "BulkUpdateUsersRequestDtoFields",
    "BulkUpdateUsersSquadsRequestDto",
    "CloneSubscriptionPageConfigRequestDto",
    "CloneSubscriptionPageConfigResponseDtoResponse",
    "CreateApiTokenRequestDto",
    "CreateApiTokenResponseDtoResponse",
    "CreateConfigProfileRequestDto",
    "CreateConfigProfileResponseDtoResponse",
    "CreateConfigProfileResponseDtoResponseInbounds",
    "CreateConfigProfileResponseDtoResponseNodes",
    "CreateExternalSquadRequestDto",
    "CreateExternalSquadResponseDtoResponse",
    "CreateExternalSquadResponseDtoResponseCustomRemarks",
    "CreateExternalSquadResponseDtoResponseHostOverrides",
    "CreateExternalSquadResponseDtoResponseHwidSettings",
    "CreateExternalSquadResponseDtoResponseInfo",
    "CreateExternalSquadResponseDtoResponseSubscriptionSettings",
    "CreateExternalSquadResponseDtoResponseTemplates",
    "CreateHostRequestDto",
    "CreateHostRequestDtoInbound",
    "CreateInfraBillingHistoryRecordRequestDto",
    "CreateInfraBillingHistoryRecordResponseDtoResponse",
    "CreateInfraBillingHistoryRecordResponseDtoResponseRecords",
    "CreateInfraBillingHistoryRecordResponseDtoResponseRecordsProvider",
    "CreateInfraBillingNodeRequestDto",
    "CreateInfraBillingNodeResponseDtoResponse",
    "CreateInfraBillingNodeResponseDtoResponseBillingNodes",
    "CreateInfraBillingNodeResponseDtoResponseBillingNodesProvider",
    "CreateInfraBillingNodeResponseDtoResponseStats",
    "CreateInfraProviderRequestDto",
    "CreateInfraProviderResponseDtoResponse",
    "CreateInfraProviderResponseDtoResponseBillingHistory",
    "CreateInfraProviderResponseDtoResponseBillingNodes",
    "CreateInternalSquadRequestDto",
    "CreateInternalSquadResponseDtoResponse",
    "CreateInternalSquadResponseDtoResponseInfo",
    "CreateNodeRequestDto",
    "CreateNodeRequestDtoConfigProfile",
    "CreateNodeResponseDtoResponse",
    "CreateNodeResponseDtoResponseConfigProfile",
    "CreateNodeResponseDtoResponseProvider",
    "CreateSnippetRequestDto",
    "CreateSnippetResponseDtoResponse",
    "CreateSnippetResponseDtoResponseSnippets",
    "CreateSubscriptionPageConfigRequestDto",
    "CreateSubscriptionPageConfigResponseDtoResponse",
    "CreateSubscriptionTemplateRequestDto",
    "CreateSubscriptionTemplateResponseDtoResponse",
    "CreateUserHwidDeviceRequestDto",
    "CreateUserHwidDeviceResponseDtoResponse",
    "CreateUserHwidDeviceResponseDtoResponseDevices",
    "CreateUserRequestDto",
    "CreateUserResponseDtoResponse",
    "CreateUserResponseDtoResponseActiveInternalSquads",
    "CreateUserResponseDtoResponseUserTraffic",
    "DebugSrrMatcherRequestDto",
    "DebugSrrMatcherRequestDtoResponseRules",
    "DebugSrrMatcherRequestDtoResponseRulesRules",
    "DebugSrrMatcherRequestDtoResponseRulesRulesConditions",
    "DebugSrrMatcherRequestDtoResponseRulesRulesResponseModifications",
    "DebugSrrMatcherRequestDtoResponseRulesRulesResponseModificationsHeaders",
    "DebugSrrMatcherRequestDtoResponseRulesSettings",
    "DebugSrrMatcherResponseDtoResponse",
    "DeleteAllUserHwidDevicesRequestDto",
    "DeleteConfigProfileResponseDtoResponse",
    "DeletePasskeyRequestDto",
    "DeletePasskeyResponseDtoResponse",
    "DeletePasskeyResponseDtoResponsePasskeys",
    "DeleteSnippetRequestDto",
    "DeleteUserHwidDeviceRequestDto",
    "DropConnectionsRequestDto",
    "DropConnectionsRequestDtoDropBy",
    "DropConnectionsRequestDtoDropBy2",
    "DropConnectionsRequestDtoTargetNodes",
    "DropConnectionsRequestDtoTargetNodes2",
    "EncryptHappCryptoLinkRequestDto",
    "EncryptHappCryptoLinkResponseDtoResponse",
    "FetchIpsResponseDtoResponse",
    "FetchIpsResultResponseDtoResponse",
    "FetchIpsResultResponseDtoResponseProgress",
    "FetchIpsResultResponseDtoResponseResult",
    "FetchIpsResultResponseDtoResponseResultNodes",
    "FindAllApiTokensResponseDtoResponse",
    "FindAllApiTokensResponseDtoResponseApiKeys",
    "FindAllApiTokensResponseDtoResponseDocs",
    "GenerateX25519ResponseDtoResponse",
    "GenerateX25519ResponseDtoResponseKeypairs",
    "GetAllHostTagsResponseDtoResponse",
    "GetAllInboundsResponseDtoResponse",
    "GetAllInboundsResponseDtoResponseInbounds",
    "GetAllSubscriptionsResponseDtoResponse",
    "GetAllSubscriptionsResponseDtoResponseSubscriptions",
    "GetAllSubscriptionsResponseDtoResponseSubscriptionsUser",
    "GetAllUsersResponseDtoResponse",
    "GetBandwidthStatsResponseDtoResponse",
    "GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays",
    "GetConfigProfilesResponseDtoResponse",
    "GetConnectionKeysByUuidResponseDtoResponse",
    "GetExternalSquadsResponseDtoResponse",
    "GetHwidDevicesStatsResponseDtoResponse",
    "GetHwidDevicesStatsResponseDtoResponseByApp",
    "GetHwidDevicesStatsResponseDtoResponseByPlatform",
    "GetHwidDevicesStatsResponseDtoResponseStats",
    "GetInfraProvidersResponseDtoResponse",
    "GetInternalSquadAccessibleNodesResponseDtoResponse",
    "GetInternalSquadAccessibleNodesResponseDtoResponseAccessibleNodes",
    "GetInternalSquadsResponseDtoResponse",
    "GetLegacyStatsNodesUsersUsageResponseDtoResponse",
    "GetLegacyStatsUserUsageResponseDtoResponse",
    "GetMetadataResponseDtoResponse",
    "GetMetadataResponseDtoResponseBuild",
    "GetMetadataResponseDtoResponseGit",
    "GetMetadataResponseDtoResponseGitBackend",
    "GetMetadataResponseDtoResponseGitFrontend",
    "GetNodesStatisticsResponseDtoResponse",
    "GetNodesStatisticsResponseDtoResponseLastSevenDays",
    "GetPubKeyResponseDtoResponse",
    "GetRawSubscriptionByShortUuidResponseDtoResponse",
    "GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHosts",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsAdditionalParams",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsDbData",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsPassword",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptions",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsProtocolOptionsSs",
    "GetRawSubscriptionByShortUuidResponseDtoResponseRawHostsRawSettings",
    "GetRemnawaveHealthResponseDtoResponse",
    "GetRemnawaveHealthResponseDtoResponsePm2Stats",
    "GetRemnawaveSettingsResponseDtoResponse",
    "GetRemnawaveSettingsResponseDtoResponseBrandingSettings",
    "GetRemnawaveSettingsResponseDtoResponseOauth2Settings",
    "GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric",
    "GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub",
    "GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak",
    "GetRemnawaveSettingsResponseDtoResponseOauth2SettingsPocketid",
    "GetRemnawaveSettingsResponseDtoResponsePasskeySettings",
    "GetRemnawaveSettingsResponseDtoResponsePasswordSettings",
    "GetRemnawaveSettingsResponseDtoResponseTgAuthSettings",
    "GetStatsNodeUsersUsageResponseDtoResponse",
    "GetStatsNodeUsersUsageResponseDtoResponseTopUsers",
    "GetStatsNodesRealtimeUsageResponseDtoResponse",
    "GetStatsNodesUsageResponseDtoResponse",
    "GetStatsNodesUsageResponseDtoResponseSeries",
    "GetStatsNodesUsageResponseDtoResponseTopNodes",
    "GetStatsResponseDtoResponse",
    "GetStatsResponseDtoResponseCpu",
    "GetStatsResponseDtoResponseMemory",
    "GetStatsResponseDtoResponseNodes",
    "GetStatsResponseDtoResponseOnlineStats",
    "GetStatsResponseDtoResponseUsers",
    "GetStatusResponseDtoResponse",
    "GetStatusResponseDtoResponseAuthentication",
    "GetStatusResponseDtoResponseAuthenticationOauth2",
    "GetStatusResponseDtoResponseAuthenticationTgAuth",
    "GetStatusResponseDtoResponseBranding",
    "GetSubpageConfigByShortUuidResponseDtoResponse",
    "GetSubscriptionPageConfigsResponseDtoResponse",
    "GetSubscriptionRequestHistoryStatsResponseDtoResponse",
    "GetSubscriptionRequestHistoryStatsResponseDtoResponseHourlyRequestStats",
    "GetSubscriptionSettingsResponseDtoResponse",
    "GetTemplatesResponseDtoResponse",
    "GetUserAccessibleNodesResponseDtoResponse",
    "GetUserAccessibleNodesResponseDtoResponseActiveNodes",
    "GetUserAccessibleNodesResponseDtoResponseActiveNodesActiveSquads",
    "LoginRequestDto",
    "LoginResponseDtoResponse",
    "OAuth2AuthorizeRequestDto",
    "OAuth2AuthorizeResponseDtoResponse",
    "OAuth2CallbackRequestDto",
    "ProfileModificationRequestDto",
    "RegisterRequestDto",
    "RemnawaveWebhookCrmEventsDto",
    "RemnawaveWebhookCrmEventsDtoData",
    "RemnawaveWebhookErrorsEventsDto",
    "RemnawaveWebhookErrorsEventsDtoData",
    "RemnawaveWebhookNodeEventsDto",
    "RemnawaveWebhookServiceEventsDto",
    "RemnawaveWebhookServiceEventsDtoData",
    "RemnawaveWebhookServiceEventsDtoDataLoginAttempt",
    "RemnawaveWebhookServiceEventsDtoDataSubpageConfig",
    "RemnawaveWebhookUserEventsDto",
    "RemnawaveWebhookUserEventsDtoMeta",
    "RemnawaveWebhookUserHwidDevicesEventsDto",
    "RemnawaveWebhookUserHwidDevicesEventsDtoData",
    "ReorderConfigProfilesRequestDto",
    "ReorderConfigProfilesRequestDtoItems",
    "ReorderExternalSquadsRequestDto",
    "ReorderHostRequestDto",
    "ReorderHostResponseDtoResponse",
    "ReorderInternalSquadsRequestDto",
    "ReorderNodeRequestDto",
    "ReorderSubscriptionPageConfigsRequestDto",
    "ReorderSubscriptionTemplatesRequestDto",
    "RestartAllNodesRequestBodyDto",
    "SetInboundToManyHostsRequestDto",
    "SetPortToManyHostsRequestDto",
    "TelegramCallbackRequestDto",
    "UpdateConfigProfileRequestDto",
    "UpdateExternalSquadRequestDto",
    "UpdateHostRequestDto",
    "UpdateInfraBillingNodeRequestDto",
    "UpdateInfraProviderRequestDto",
    "UpdateInternalSquadRequestDto",
    "UpdateNodeRequestDto",
    "UpdatePasskeyRequestDto",
    "UpdateRemnawaveSettingsRequestDto",
    "UpdateSnippetRequestDto",
    "UpdateSubscriptionPageConfigRequestDto",
    "UpdateSubscriptionSettingsRequestDto",
    "UpdateTemplateRequestDto",
    "UpdateUserRequestDto",
    "VerifyPasskeyAuthenticationRequestDto",
    "VerifyPasskeyRegistrationRequestDto",
    "VerifyPasskeyRegistrationResponseDtoResponse",
)
