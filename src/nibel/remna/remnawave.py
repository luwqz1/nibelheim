from saronia import API

from .auth import AuthorizationModel

remnawave = API.endpoint("/api").bind_auth(AuthorizationModel)

__all__ = ("remnawave",)
