import http


class RemnawaveError(Exception):
    def __init__(self, error: object, code: int) -> None:
        self.error = error
        self.code = code
        self.status_code = http.HTTPStatus(code)
        super().__init__(self.error)

    def __str__(self) -> str:
        return f"[{self.code}] ({self.status_code.name}) {self.error}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}: {self}"


__all__ = ("RemnawaveError",)
