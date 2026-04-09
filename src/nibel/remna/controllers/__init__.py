import saronia

from ..remnawave import remnawave
from .auth_controller import AuthController
from .bandwidth_stats_controller import BandwidthStatsController
from .config_profiles_controller import ConfigProfilesController
from .external_squads_controller import ExternalSquadsController
from .hosts_bulk_controller import HostsBulkController
from .hosts_controller import HostsController
from .hwid_devices_controller import HwidDevicesController
from .infra_billing_controller import InfraBillingController
from .internal_squads_controller import InternalSquadsController
from .ip_control_controller import IpControlController
from .keygen_controller import KeygenController
from .metadata_controller import MetadataController
from .node_plugins_controller import NodePluginsController
from .nodes_controller import NodesController
from .passkeys_controller import PasskeysController
from .remnawave_settings_controller import RemnawaveSettingsController
from .snippets_controller import SnippetsController
from .sub_controller import SubController
from .subscription_page_configs_controller import SubscriptionPageConfigsController
from .subscription_request_history_controller import SubscriptionRequestHistoryController
from .subscription_settings_controller import SubscriptionSettingsController
from .subscription_templates_controller import SubscriptionTemplatesController
from .subscriptions_controller import SubscriptionsController
from .system_controller import SystemController
from .tokens_controller import TokensController
from .users_bulk_controller import UsersBulkController
from .users_controller import UsersController


class APIControllers:
    def __init__(self, client: saronia.ABCClient) -> None:
        self.auth = AuthController()
        self.bandwidth_stats = BandwidthStatsController()
        self.config_profiles = ConfigProfilesController()
        self.external_squads = ExternalSquadsController()
        self.hosts_bulk = HostsBulkController()
        self.hosts = HostsController()
        self.hwid_devices = HwidDevicesController()
        self.infra_billing = InfraBillingController()
        self.internal_squads = InternalSquadsController()
        self.ip_control = IpControlController()
        self.keygen = KeygenController()
        self.metadata = MetadataController()
        self.node_plugins = NodePluginsController()
        self.nodes = NodesController()
        self.passkeys = PasskeysController()
        self.remnawave_settings = RemnawaveSettingsController()
        self.snippets = SnippetsController()
        self.sub = SubController()
        self.subscription_page_configs = SubscriptionPageConfigsController()
        self.subscription_request_history = SubscriptionRequestHistoryController()
        self.subscription_settings = SubscriptionSettingsController()
        self.subscription_templates = SubscriptionTemplatesController()
        self.subscriptions = SubscriptionsController()
        self.system = SystemController()
        self.tokens = TokensController()
        self.users_bulk = UsersBulkController()
        self.users = UsersController()

        remnawave.build(client)


__all__ = (
    "APIControllers",
    "AuthController",
    "BandwidthStatsController",
    "ConfigProfilesController",
    "ExternalSquadsController",
    "HostsBulkController",
    "HostsController",
    "HwidDevicesController",
    "InfraBillingController",
    "InternalSquadsController",
    "IpControlController",
    "KeygenController",
    "MetadataController",
    "NodePluginsController",
    "NodesController",
    "PasskeysController",
    "RemnawaveSettingsController",
    "SnippetsController",
    "SubController",
    "SubscriptionPageConfigsController",
    "SubscriptionRequestHistoryController",
    "SubscriptionSettingsController",
    "SubscriptionTemplatesController",
    "SubscriptionsController",
    "SystemController",
    "TokensController",
    "UsersBulkController",
    "UsersController",
)
