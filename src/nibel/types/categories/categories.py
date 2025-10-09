from __future__ import annotations

import abc
import typing

if typing.TYPE_CHECKING:
    from nibel.api import Remnawave


class APICategories(abc.ABC):
    @property
    @abc.abstractmethod
    def api(self) -> Remnawave:
        pass


__all__ = ("APICategories",)
