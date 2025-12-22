from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from nibel.remna import Remnawave


class BaseCategory:
    def __init__(self, api: Remnawave) -> None:
        self.api = api


__all__ = ("BaseCategory",)
