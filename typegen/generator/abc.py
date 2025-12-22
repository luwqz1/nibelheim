import abc
import typing

if typing.TYPE_CHECKING:
    import pathlib

    from jinja2 import Environment


type API = typing.Any
type Context = dict[str, typing.Any]


class ABCGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(
        self,
        api: API,
        context: Context,
        environment: Environment,
        workdir: pathlib.Path,
    ) -> None:
        pass


__all__ = ("ABCGenerator",)
