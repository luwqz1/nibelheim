import msgspec

from typegen.cfg.generator import GeneratorConfig
from typegen.model import Model


class RemnawaveAPI(Model):
    version: str
    oas_url: str


class Config(Model):
    remnawave: RemnawaveAPI = msgspec.field(name="remnawave-api")
    generator: GeneratorConfig


__all__ = ("Config",)
