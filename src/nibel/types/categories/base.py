from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from nibel.api import Remnawave


class BaseCategory:
    def __init__(self, api: Remnawave) -> None:
        self.api = api

    def get_method_params(self) -> dict[str, typing.Any]: ...


__all__ = ("BaseCategory",)
