import typing

from nibel.types.categories.categories import APICategories


class Remnawave(APICategories):
    @property
    def api(self) -> typing.Self:
        return self


__all__ = ("Remnawave",)
