from __future__ import annotations

import typing

import msgspex

from .objects import (
    AddUsersToExternalSquadResponseDtoResponse,
    BulkDeleteHostsResponseDtoResponse,
    BulkDeleteUsersByStatusResponseDtoResponse,
    CloneNodePluginResponseDtoResponse,
    CloneSubscriptionPageConfigResponseDtoResponse,
    CreateApiTokenResponseDtoResponse,
    CreateConfigProfileResponseDtoResponse,
    CreateExternalSquadResponseDtoResponse,
    CreateInfraBillingHistoryRecordResponseDtoResponse,
    CreateInfraBillingNodeResponseDtoResponse,
    CreateInfraProviderResponseDtoResponse,
    CreateInternalSquadResponseDtoResponse,
    CreateNodePluginResponseDtoResponse,
    CreateNodeResponseDtoResponse,
    CreateSnippetResponseDtoResponse,
    CreateSubscriptionPageConfigResponseDtoResponse,
    CreateSubscriptionTemplateResponseDtoResponse,
    CreateUserHwidDeviceResponseDtoResponse,
    CreateUserResponseDtoResponse,
    DebugSrrMatcherResponseDtoResponse,
    DeleteConfigProfileResponseDtoResponse,
    DeletePasskeyResponseDtoResponse,
    EncryptHappCryptoLinkResponseDtoResponse,
    FetchIpsResponseDtoResponse,
    FetchIpsResultResponseDtoResponse,
    FetchUsersIpsResultResponseDtoResponse,
    FindAllApiTokensResponseDtoResponse,
    GenerateX25519ResponseDtoResponse,
    GetAllHostTagsResponseDtoResponse,
    GetAllInboundsResponseDtoResponse,
    GetAllSubscriptionsResponseDtoResponse,
    GetAllSubscriptionsResponseDtoResponseSubscriptions,
    GetAllUsersResponseDtoResponse,
    GetBandwidthStatsResponseDtoResponse,
    GetConfigProfilesResponseDtoResponse,
    GetConnectionKeysByUuidResponseDtoResponse,
    GetExternalSquadsResponseDtoResponse,
    GetHwidDevicesStatsResponseDtoResponse,
    GetInfraProvidersResponseDtoResponse,
    GetInternalSquadAccessibleNodesResponseDtoResponse,
    GetInternalSquadsResponseDtoResponse,
    GetLegacyStatsNodesUsersUsageResponseDtoResponse,
    GetLegacyStatsUserUsageResponseDtoResponse,
    GetMetadataResponseDtoResponse,
    GetNodePluginsResponseDtoResponse,
    GetNodesStatisticsResponseDtoResponse,
    GetPubKeyResponseDtoResponse,
    GetRawSubscriptionByShortUuidResponseDtoResponse,
    GetRecapResponseDtoResponse,
    GetRemnawaveHealthResponseDtoResponse,
    GetRemnawaveSettingsResponseDtoResponse,
    GetStatsNodesUsageResponseDtoResponse,
    GetStatsNodeUsersUsageResponseDtoResponse,
    GetStatsResponseDtoResponse,
    GetStatusResponseDtoResponse,
    GetSubpageConfigByShortUuidResponseDtoResponse,
    GetSubscriptionPageConfigsResponseDtoResponse,
    GetSubscriptionRequestHistoryStatsResponseDtoResponse,
    GetSubscriptionSettingsResponseDtoResponse,
    GetTemplatesResponseDtoResponse,
    GetTorrentBlockerReportsStatsResponseDtoResponse,
    GetUserAccessibleNodesResponseDtoResponse,
    LoginResponseDtoResponse,
    OAuth2AuthorizeResponseDtoResponse,
    ReorderHostResponseDtoResponse,
    ReorderNodeRequestDto,
    ResolveUserResponseDtoResponse,
    UpsertUserMetadataRequestBodyDto,
    VerifyPasskeyRegistrationResponseDtoResponse,
)


class AddUsersToExternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class AddUsersToInternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkAllExtendExpirationDateResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkAllResetTrafficUsersResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkAllUpdateUsersResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkDeleteHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class BulkDeleteUsersByStatusResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkDeleteUsersResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkDisableHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class BulkEnableHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class BulkExtendExpirationDateResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkNodesActionsResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkNodesUpdateResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class BulkResetTrafficUsersResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkRevokeUsersSubscriptionResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkUpdateUsersResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class BulkUpdateUsersSquadsResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteUsersByStatusResponseDtoResponse


class CloneNodePluginResponseDto(msgspex.Model, kw_only=True):
    response: CloneNodePluginResponseDtoResponse


class CloneSubscriptionPageConfigResponseDto(msgspex.Model, kw_only=True):
    response: CloneSubscriptionPageConfigResponseDtoResponse


class CreateApiTokenResponseDto(msgspex.Model, kw_only=True):
    response: CreateApiTokenResponseDtoResponse


class CreateConfigProfileResponseDto(msgspex.Model, kw_only=True):
    response: CreateConfigProfileResponseDtoResponse


class CreateExternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: CreateExternalSquadResponseDtoResponse


class CreateHostResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteHostsResponseDtoResponse


class CreateInfraBillingHistoryRecordResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class CreateInfraBillingNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingNodeResponseDtoResponse


class CreateInfraProviderResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraProviderResponseDtoResponse


class CreateInternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: CreateInternalSquadResponseDtoResponse


class CreateNodePluginResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodePluginResponseDtoResponse


class CreateNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodeResponseDtoResponse


class CreateSnippetResponseDto(msgspex.Model, kw_only=True):
    response: CreateSnippetResponseDtoResponse


class CreateSubscriptionPageConfigResponseDto(msgspex.Model, kw_only=True):
    response: CreateSubscriptionPageConfigResponseDtoResponse


class CreateSubscriptionTemplateResponseDto(msgspex.Model, kw_only=True):
    response: CreateSubscriptionTemplateResponseDtoResponse


class CreateUserHwidDeviceResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserHwidDeviceResponseDtoResponse


class CreateUserResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class DebugSrrMatcherResponseDto(msgspex.Model, kw_only=True):
    response: DebugSrrMatcherResponseDtoResponse


class DeleteAllUserHwidDevicesResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserHwidDeviceResponseDtoResponse


class DeleteApiTokenResponseDto(msgspex.Model, kw_only=True):
    response: bool


class DeleteConfigProfileResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteExternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteHostResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteInfraBillingHistoryRecordByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class DeleteInfraBillingNodeByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingNodeResponseDtoResponse


class DeleteInfraProviderByUuidResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteInternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteNodePluginResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteNodeResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeletePasskeyResponseDto(msgspex.Model, kw_only=True):
    response: DeletePasskeyResponseDtoResponse


class DeleteSnippetResponseDto(msgspex.Model, kw_only=True):
    response: CreateSnippetResponseDtoResponse


class DeleteSubscriptionPageConfigResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteSubscriptionTemplateResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DeleteUserHwidDeviceResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserHwidDeviceResponseDtoResponse


class DeleteUserResponseDto(msgspex.Model, kw_only=True):
    response: DeleteConfigProfileResponseDtoResponse


class DisableNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodeResponseDtoResponse


class DisableUserResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class DropConnectionsResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class EnableNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodeResponseDtoResponse


class EnableUserResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class EncryptHappCryptoLinkResponseDto(msgspex.Model, kw_only=True):
    response: EncryptHappCryptoLinkResponseDtoResponse


class FetchIpsResponseDto(msgspex.Model, kw_only=True):
    response: FetchIpsResponseDtoResponse


class FetchIpsResultResponseDto(msgspex.Model, kw_only=True):
    response: FetchIpsResultResponseDtoResponse


class FetchUsersIpsResponseDto(msgspex.Model, kw_only=True):
    response: FetchIpsResponseDtoResponse


class FetchUsersIpsResultResponseDto(msgspex.Model, kw_only=True):
    response: FetchUsersIpsResultResponseDtoResponse


class FindAllApiTokensResponseDto(msgspex.Model, kw_only=True):
    response: FindAllApiTokensResponseDtoResponse


class GenerateX25519ResponseDto(msgspex.Model, kw_only=True):
    response: GenerateX25519ResponseDtoResponse


class GetAllHostTagsResponseDto(msgspex.Model, kw_only=True):
    response: GetAllHostTagsResponseDtoResponse


class GetAllHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class GetAllHwidDevicesResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserHwidDeviceResponseDtoResponse


class GetAllInboundsResponseDto(msgspex.Model, kw_only=True):
    response: GetAllInboundsResponseDtoResponse


class GetAllNodesResponseDto(msgspex.Model, kw_only=True):
    response: list[CreateNodeResponseDtoResponse]


class GetAllNodesTagsResponseDto(msgspex.Model, kw_only=True):
    response: GetAllHostTagsResponseDtoResponse


class GetAllPasskeysResponseDto(msgspex.Model, kw_only=True):
    response: DeletePasskeyResponseDtoResponse


class GetAllSubscriptionsResponseDto(msgspex.Model, kw_only=True):
    response: GetAllSubscriptionsResponseDtoResponse


class GetAllTagsResponseDto(msgspex.Model, kw_only=True):
    response: GetAllHostTagsResponseDtoResponse


class GetAllUsersResponseDto(msgspex.Model, kw_only=True):
    response: GetAllUsersResponseDtoResponse


class GetBandwidthStatsResponseDto(msgspex.Model, kw_only=True):
    response: GetBandwidthStatsResponseDtoResponse


class GetComputedConfigProfileByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateConfigProfileResponseDtoResponse


class GetConfigProfileByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateConfigProfileResponseDtoResponse


class GetConfigProfilesResponseDto(msgspex.Model, kw_only=True):
    response: GetConfigProfilesResponseDtoResponse


class GetConnectionKeysByUuidResponseDto(msgspex.Model, kw_only=True):
    response: GetConnectionKeysByUuidResponseDtoResponse


class GetExternalSquadByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateExternalSquadResponseDtoResponse


class GetExternalSquadsResponseDto(msgspex.Model, kw_only=True):
    response: GetExternalSquadsResponseDtoResponse


class GetHwidDevicesStatsResponseDto(msgspex.Model, kw_only=True):
    response: GetHwidDevicesStatsResponseDtoResponse


class GetInboundsByProfileUuidResponseDto(msgspex.Model, kw_only=True):
    response: GetAllInboundsResponseDtoResponse


class GetInfraBillingHistoryRecordsResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class GetInfraBillingNodesResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingNodeResponseDtoResponse


class GetInfraProviderByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraProviderResponseDtoResponse


class GetInfraProvidersResponseDto(msgspex.Model, kw_only=True):
    response: GetInfraProvidersResponseDtoResponse


class GetInternalSquadAccessibleNodesResponseDto(msgspex.Model, kw_only=True):
    response: GetInternalSquadAccessibleNodesResponseDtoResponse


class GetInternalSquadByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateInternalSquadResponseDtoResponse


class GetInternalSquadsResponseDto(msgspex.Model, kw_only=True):
    response: GetInternalSquadsResponseDtoResponse


class GetLegacyStatsNodesUsersUsageResponseDto(msgspex.Model, kw_only=True):
    response: list[GetLegacyStatsNodesUsersUsageResponseDtoResponse]


class GetLegacyStatsUserUsageResponseDto(msgspex.Model, kw_only=True):
    response: list[GetLegacyStatsUserUsageResponseDtoResponse]


class GetMetadataResponseDto(msgspex.Model, kw_only=True):
    response: GetMetadataResponseDtoResponse


class GetNodeMetadataResponseDto(msgspex.Model, kw_only=True):
    response: UpsertUserMetadataRequestBodyDto


class GetNodePluginResponseDto(msgspex.Model, kw_only=True):
    response: CloneNodePluginResponseDtoResponse


class GetNodePluginsResponseDto(msgspex.Model, kw_only=True):
    response: GetNodePluginsResponseDtoResponse


class GetNodesMetricsResponseDto(msgspex.Model, kw_only=True):
    response: ReorderNodeRequestDto


class GetNodesStatisticsResponseDto(msgspex.Model, kw_only=True):
    response: GetNodesStatisticsResponseDtoResponse


class GetOneHostResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteHostsResponseDtoResponse


class GetOneNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodeResponseDtoResponse


class GetPasskeyAuthenticationOptionsResponseDto(msgspex.Model, kw_only=True):
    response: typing.Any


class GetPasskeyRegistrationOptionsResponseDto(msgspex.Model, kw_only=True):
    response: typing.Any


class GetPubKeyResponseDto(msgspex.Model, kw_only=True):
    response: GetPubKeyResponseDtoResponse


class GetRawSubscriptionByShortUuidResponseDto(msgspex.Model, kw_only=True):
    response: GetRawSubscriptionByShortUuidResponseDtoResponse


class GetRecapResponseDto(msgspex.Model, kw_only=True):
    response: GetRecapResponseDtoResponse


class GetRemnawaveHealthResponseDto(msgspex.Model, kw_only=True):
    response: GetRemnawaveHealthResponseDtoResponse


class GetRemnawaveSettingsResponseDto(msgspex.Model, kw_only=True):
    response: GetRemnawaveSettingsResponseDtoResponse


class GetSnippetsResponseDto(msgspex.Model, kw_only=True):
    response: CreateSnippetResponseDtoResponse


class GetStatsNodeUsersUsageResponseDto(msgspex.Model, kw_only=True):
    response: GetStatsNodeUsersUsageResponseDtoResponse


class GetStatsNodesUsageResponseDto(msgspex.Model, kw_only=True):
    response: GetStatsNodesUsageResponseDtoResponse


class GetStatsResponseDto(msgspex.Model, kw_only=True):
    response: GetStatsResponseDtoResponse


class GetStatsUserUsageResponseDto(msgspex.Model, kw_only=True):
    response: GetStatsNodesUsageResponseDtoResponse


class GetStatusResponseDto(msgspex.Model, kw_only=True):
    response: GetStatusResponseDtoResponse


class GetSubpageConfigByShortUuidResponseDto(msgspex.Model, kw_only=True):
    response: GetSubpageConfigByShortUuidResponseDtoResponse


class GetSubscriptionByShortUuidProtectedResponseDto(msgspex.Model, kw_only=True):
    response: GetAllSubscriptionsResponseDtoResponseSubscriptions


class GetSubscriptionByUsernameResponseDto(msgspex.Model, kw_only=True):
    response: GetAllSubscriptionsResponseDtoResponseSubscriptions


class GetSubscriptionByUuidResponseDto(msgspex.Model, kw_only=True):
    response: GetAllSubscriptionsResponseDtoResponseSubscriptions


class GetSubscriptionInfoResponseDto(msgspex.Model, kw_only=True):
    response: GetAllSubscriptionsResponseDtoResponseSubscriptions


class GetSubscriptionPageConfigResponseDto(msgspex.Model, kw_only=True):
    response: CloneSubscriptionPageConfigResponseDtoResponse


class GetSubscriptionPageConfigsResponseDto(msgspex.Model, kw_only=True):
    response: GetSubscriptionPageConfigsResponseDtoResponse


class GetSubscriptionRequestHistoryResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class GetSubscriptionRequestHistoryStatsResponseDto(msgspex.Model, kw_only=True):
    response: GetSubscriptionRequestHistoryStatsResponseDtoResponse


class GetSubscriptionSettingsResponseDto(msgspex.Model, kw_only=True):
    response: GetSubscriptionSettingsResponseDtoResponse


class GetTemplateResponseDto(msgspex.Model, kw_only=True):
    response: CreateSubscriptionTemplateResponseDtoResponse


class GetTemplatesResponseDto(msgspex.Model, kw_only=True):
    response: GetTemplatesResponseDtoResponse


class GetTopUsersByHwidDevicesResponseDto(msgspex.Model, kw_only=True):
    response: GetAllUsersResponseDtoResponse


class GetTorrentBlockerReportsResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class GetTorrentBlockerReportsStatsResponseDto(msgspex.Model, kw_only=True):
    response: GetTorrentBlockerReportsStatsResponseDtoResponse


class GetUserAccessibleNodesResponseDto(msgspex.Model, kw_only=True):
    response: GetUserAccessibleNodesResponseDtoResponse


class GetUserByEmailResponseDto(msgspex.Model, kw_only=True):
    response: list[CreateUserResponseDtoResponse]


class GetUserByIdResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class GetUserByShortUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class GetUserByTagResponseDto(msgspex.Model, kw_only=True):
    response: list[CreateUserResponseDtoResponse]


class GetUserByTelegramIdResponseDto(msgspex.Model, kw_only=True):
    response: list[CreateUserResponseDtoResponse]


class GetUserByUsernameResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class GetUserByUuidResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class GetUserHwidDevicesResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserHwidDeviceResponseDtoResponse


class GetUserMetadataResponseDto(msgspex.Model, kw_only=True):
    response: UpsertUserMetadataRequestBodyDto


class GetUserSubscriptionRequestHistoryResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class LoginResponseDto(msgspex.Model, kw_only=True):
    response: LoginResponseDtoResponse


class OAuth2AuthorizeResponseDto(msgspex.Model, kw_only=True):
    response: OAuth2AuthorizeResponseDtoResponse


class OAuth2CallbackResponseDto(msgspex.Model, kw_only=True):
    response: LoginResponseDtoResponse


class PluginExecutorResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class ProfileModificationResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class RegisterResponseDto(msgspex.Model, kw_only=True):
    response: LoginResponseDtoResponse


class RemoveUsersFromExternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class RemoveUsersFromInternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class ReorderConfigProfilesResponseDto(msgspex.Model, kw_only=True):
    response: GetConfigProfilesResponseDtoResponse


class ReorderExternalSquadsResponseDto(msgspex.Model, kw_only=True):
    response: GetExternalSquadsResponseDtoResponse


class ReorderHostResponseDto(msgspex.Model, kw_only=True):
    response: ReorderHostResponseDtoResponse


class ReorderInternalSquadsResponseDto(msgspex.Model, kw_only=True):
    response: GetInternalSquadsResponseDtoResponse


class ReorderNodePluginsResponseDto(msgspex.Model, kw_only=True):
    response: GetNodePluginsResponseDtoResponse


class ReorderNodeResponseDto(msgspex.Model, kw_only=True):
    response: list[CreateNodeResponseDtoResponse]


class ReorderSubscriptionPageConfigsResponseDto(msgspex.Model, kw_only=True):
    response: GetSubscriptionPageConfigsResponseDtoResponse


class ReorderSubscriptionTemplatesResponseDto(msgspex.Model, kw_only=True):
    response: GetTemplatesResponseDtoResponse


class ResetNodeTrafficResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class ResetUserTrafficResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class ResolveUserResponseDto(msgspex.Model, kw_only=True):
    response: ResolveUserResponseDtoResponse


class RestartAllNodesResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class RestartNodeResponseDto(msgspex.Model, kw_only=True):
    response: AddUsersToExternalSquadResponseDtoResponse


class RevokeUserSubscriptionResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class SetInboundToManyHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class SetPortToManyHostsResponseDto(msgspex.Model, kw_only=True):
    response: list[BulkDeleteHostsResponseDtoResponse]


class TruncateTorrentBlockerReportsResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingHistoryRecordResponseDtoResponse


class UpdateConfigProfileResponseDto(msgspex.Model, kw_only=True):
    response: CreateConfigProfileResponseDtoResponse


class UpdateExternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: CreateExternalSquadResponseDtoResponse


class UpdateHostResponseDto(msgspex.Model, kw_only=True):
    response: BulkDeleteHostsResponseDtoResponse


class UpdateInfraBillingNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraBillingNodeResponseDtoResponse


class UpdateInfraProviderResponseDto(msgspex.Model, kw_only=True):
    response: CreateInfraProviderResponseDtoResponse


class UpdateInternalSquadResponseDto(msgspex.Model, kw_only=True):
    response: CreateInternalSquadResponseDtoResponse


class UpdateNodePluginResponseDto(msgspex.Model, kw_only=True):
    response: CloneNodePluginResponseDtoResponse


class UpdateNodeResponseDto(msgspex.Model, kw_only=True):
    response: CreateNodeResponseDtoResponse


class UpdatePasskeyResponseDto(msgspex.Model, kw_only=True):
    response: DeletePasskeyResponseDtoResponse


class UpdateRemnawaveSettingsResponseDto(msgspex.Model, kw_only=True):
    response: GetRemnawaveSettingsResponseDtoResponse


class UpdateSnippetResponseDto(msgspex.Model, kw_only=True):
    response: CreateSnippetResponseDtoResponse


class UpdateSubscriptionPageConfigResponseDto(msgspex.Model, kw_only=True):
    response: CloneSubscriptionPageConfigResponseDtoResponse


class UpdateSubscriptionSettingsResponseDto(msgspex.Model, kw_only=True):
    response: GetSubscriptionSettingsResponseDtoResponse


class UpdateTemplateResponseDto(msgspex.Model, kw_only=True):
    response: CreateSubscriptionTemplateResponseDtoResponse


class UpdateUserResponseDto(msgspex.Model, kw_only=True):
    response: CreateUserResponseDtoResponse


class UpsertNodeMetadataResponseDto(msgspex.Model, kw_only=True):
    response: UpsertUserMetadataRequestBodyDto


class UpsertUserMetadataResponseDto(msgspex.Model, kw_only=True):
    response: UpsertUserMetadataRequestBodyDto


class VerifyPasskeyAuthenticationResponseDto(msgspex.Model, kw_only=True):
    response: LoginResponseDtoResponse


class VerifyPasskeyRegistrationResponseDto(msgspex.Model, kw_only=True):
    response: VerifyPasskeyRegistrationResponseDtoResponse


__all__ = (
    "AddUsersToExternalSquadResponseDto",
    "AddUsersToInternalSquadResponseDto",
    "BulkAllExtendExpirationDateResponseDto",
    "BulkAllResetTrafficUsersResponseDto",
    "BulkAllUpdateUsersResponseDto",
    "BulkDeleteHostsResponseDto",
    "BulkDeleteUsersByStatusResponseDto",
    "BulkDeleteUsersResponseDto",
    "BulkDisableHostsResponseDto",
    "BulkEnableHostsResponseDto",
    "BulkExtendExpirationDateResponseDto",
    "BulkNodesActionsResponseDto",
    "BulkNodesUpdateResponseDto",
    "BulkResetTrafficUsersResponseDto",
    "BulkRevokeUsersSubscriptionResponseDto",
    "BulkUpdateUsersResponseDto",
    "BulkUpdateUsersSquadsResponseDto",
    "CloneNodePluginResponseDto",
    "CloneSubscriptionPageConfigResponseDto",
    "CreateApiTokenResponseDto",
    "CreateConfigProfileResponseDto",
    "CreateExternalSquadResponseDto",
    "CreateHostResponseDto",
    "CreateInfraBillingHistoryRecordResponseDto",
    "CreateInfraBillingNodeResponseDto",
    "CreateInfraProviderResponseDto",
    "CreateInternalSquadResponseDto",
    "CreateNodePluginResponseDto",
    "CreateNodeResponseDto",
    "CreateSnippetResponseDto",
    "CreateSubscriptionPageConfigResponseDto",
    "CreateSubscriptionTemplateResponseDto",
    "CreateUserHwidDeviceResponseDto",
    "CreateUserResponseDto",
    "DebugSrrMatcherResponseDto",
    "DeleteAllUserHwidDevicesResponseDto",
    "DeleteApiTokenResponseDto",
    "DeleteConfigProfileResponseDto",
    "DeleteExternalSquadResponseDto",
    "DeleteHostResponseDto",
    "DeleteInfraBillingHistoryRecordByUuidResponseDto",
    "DeleteInfraBillingNodeByUuidResponseDto",
    "DeleteInfraProviderByUuidResponseDto",
    "DeleteInternalSquadResponseDto",
    "DeleteNodePluginResponseDto",
    "DeleteNodeResponseDto",
    "DeletePasskeyResponseDto",
    "DeleteSnippetResponseDto",
    "DeleteSubscriptionPageConfigResponseDto",
    "DeleteSubscriptionTemplateResponseDto",
    "DeleteUserHwidDeviceResponseDto",
    "DeleteUserResponseDto",
    "DisableNodeResponseDto",
    "DisableUserResponseDto",
    "DropConnectionsResponseDto",
    "EnableNodeResponseDto",
    "EnableUserResponseDto",
    "EncryptHappCryptoLinkResponseDto",
    "FetchIpsResponseDto",
    "FetchIpsResultResponseDto",
    "FetchUsersIpsResponseDto",
    "FetchUsersIpsResultResponseDto",
    "FindAllApiTokensResponseDto",
    "GenerateX25519ResponseDto",
    "GetAllHostTagsResponseDto",
    "GetAllHostsResponseDto",
    "GetAllHwidDevicesResponseDto",
    "GetAllInboundsResponseDto",
    "GetAllNodesResponseDto",
    "GetAllNodesTagsResponseDto",
    "GetAllPasskeysResponseDto",
    "GetAllSubscriptionsResponseDto",
    "GetAllTagsResponseDto",
    "GetAllUsersResponseDto",
    "GetBandwidthStatsResponseDto",
    "GetComputedConfigProfileByUuidResponseDto",
    "GetConfigProfileByUuidResponseDto",
    "GetConfigProfilesResponseDto",
    "GetConnectionKeysByUuidResponseDto",
    "GetExternalSquadByUuidResponseDto",
    "GetExternalSquadsResponseDto",
    "GetHwidDevicesStatsResponseDto",
    "GetInboundsByProfileUuidResponseDto",
    "GetInfraBillingHistoryRecordsResponseDto",
    "GetInfraBillingNodesResponseDto",
    "GetInfraProviderByUuidResponseDto",
    "GetInfraProvidersResponseDto",
    "GetInternalSquadAccessibleNodesResponseDto",
    "GetInternalSquadByUuidResponseDto",
    "GetInternalSquadsResponseDto",
    "GetLegacyStatsNodesUsersUsageResponseDto",
    "GetLegacyStatsUserUsageResponseDto",
    "GetMetadataResponseDto",
    "GetNodeMetadataResponseDto",
    "GetNodePluginResponseDto",
    "GetNodePluginsResponseDto",
    "GetNodesMetricsResponseDto",
    "GetNodesStatisticsResponseDto",
    "GetOneHostResponseDto",
    "GetOneNodeResponseDto",
    "GetPasskeyAuthenticationOptionsResponseDto",
    "GetPasskeyRegistrationOptionsResponseDto",
    "GetPubKeyResponseDto",
    "GetRawSubscriptionByShortUuidResponseDto",
    "GetRecapResponseDto",
    "GetRemnawaveHealthResponseDto",
    "GetRemnawaveSettingsResponseDto",
    "GetSnippetsResponseDto",
    "GetStatsNodeUsersUsageResponseDto",
    "GetStatsNodesUsageResponseDto",
    "GetStatsResponseDto",
    "GetStatsUserUsageResponseDto",
    "GetStatusResponseDto",
    "GetSubpageConfigByShortUuidResponseDto",
    "GetSubscriptionByShortUuidProtectedResponseDto",
    "GetSubscriptionByUsernameResponseDto",
    "GetSubscriptionByUuidResponseDto",
    "GetSubscriptionInfoResponseDto",
    "GetSubscriptionPageConfigResponseDto",
    "GetSubscriptionPageConfigsResponseDto",
    "GetSubscriptionRequestHistoryResponseDto",
    "GetSubscriptionRequestHistoryStatsResponseDto",
    "GetSubscriptionSettingsResponseDto",
    "GetTemplateResponseDto",
    "GetTemplatesResponseDto",
    "GetTopUsersByHwidDevicesResponseDto",
    "GetTorrentBlockerReportsResponseDto",
    "GetTorrentBlockerReportsStatsResponseDto",
    "GetUserAccessibleNodesResponseDto",
    "GetUserByEmailResponseDto",
    "GetUserByIdResponseDto",
    "GetUserByShortUuidResponseDto",
    "GetUserByTagResponseDto",
    "GetUserByTelegramIdResponseDto",
    "GetUserByUsernameResponseDto",
    "GetUserByUuidResponseDto",
    "GetUserHwidDevicesResponseDto",
    "GetUserMetadataResponseDto",
    "GetUserSubscriptionRequestHistoryResponseDto",
    "LoginResponseDto",
    "OAuth2AuthorizeResponseDto",
    "OAuth2CallbackResponseDto",
    "PluginExecutorResponseDto",
    "ProfileModificationResponseDto",
    "RegisterResponseDto",
    "RemoveUsersFromExternalSquadResponseDto",
    "RemoveUsersFromInternalSquadResponseDto",
    "ReorderConfigProfilesResponseDto",
    "ReorderExternalSquadsResponseDto",
    "ReorderHostResponseDto",
    "ReorderInternalSquadsResponseDto",
    "ReorderNodePluginsResponseDto",
    "ReorderNodeResponseDto",
    "ReorderSubscriptionPageConfigsResponseDto",
    "ReorderSubscriptionTemplatesResponseDto",
    "ResetNodeTrafficResponseDto",
    "ResetUserTrafficResponseDto",
    "ResolveUserResponseDto",
    "RestartAllNodesResponseDto",
    "RestartNodeResponseDto",
    "RevokeUserSubscriptionResponseDto",
    "SetInboundToManyHostsResponseDto",
    "SetPortToManyHostsResponseDto",
    "TruncateTorrentBlockerReportsResponseDto",
    "UpdateConfigProfileResponseDto",
    "UpdateExternalSquadResponseDto",
    "UpdateHostResponseDto",
    "UpdateInfraBillingNodeResponseDto",
    "UpdateInfraProviderResponseDto",
    "UpdateInternalSquadResponseDto",
    "UpdateNodePluginResponseDto",
    "UpdateNodeResponseDto",
    "UpdatePasskeyResponseDto",
    "UpdateRemnawaveSettingsResponseDto",
    "UpdateSnippetResponseDto",
    "UpdateSubscriptionPageConfigResponseDto",
    "UpdateSubscriptionSettingsResponseDto",
    "UpdateTemplateResponseDto",
    "UpdateUserResponseDto",
    "UpsertNodeMetadataResponseDto",
    "UpsertUserMetadataResponseDto",
    "VerifyPasskeyAuthenticationResponseDto",
    "VerifyPasskeyRegistrationResponseDto",
)
