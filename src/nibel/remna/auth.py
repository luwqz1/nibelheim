from __future__ import annotations

import dataclasses

from saronia.security import *

Authorization = HTTPBearer
Prometheus = HTTPBasic


@dataclasses.dataclass
class AuthorizationModel:
    authorization: Authorization | None = None
    prometheus: Prometheus | None = None


__all__ = (
    "Authorization",
    "AuthorizationModel",
    "Prometheus",
)
