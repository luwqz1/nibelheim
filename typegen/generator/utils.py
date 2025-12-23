def makesafe_name_from_enum_value(value: str, /) -> str:
    if value[0].isdigit():
        value = f"_{value}"
    return value.replace("-", "_").replace("/", "_").upper()


__all__ = ("makesafe_name_from_enum_value",)
