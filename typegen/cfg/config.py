from typegen.cfg.generator import GeneratorConfig
from typegen.model import Model


class Config(Model):
    generator: GeneratorConfig


__all__ = ("Config",)
