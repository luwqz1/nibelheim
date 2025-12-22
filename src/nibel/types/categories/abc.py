from __future__ import annotations

import abc
import typing

if typing.TYPE_CHECKING:
    from nibel.remna import Remnawave


class ABCCategory(abc.ABC):
    @property
    @abc.abstractmethod
    def api(self) -> Remnawave:
        pass


__all__ = ("ABCCategory",)
