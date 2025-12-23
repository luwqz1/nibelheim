from nibel.types.controllers.categories import BaseCategories


class Remnawave(BaseCategories):
    def __init__(self) -> None:
        super().__init__(api=self)


__all__ = ("Remnawave",)
