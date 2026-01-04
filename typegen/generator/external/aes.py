import typing

from typegen.schema.external.aes import RemnawaveAES


class ErrorEnumEntry(typing.NamedTuple):
    name: str
    description: str
    type: typing.Literal["string"]
    enumerations: dict[str, str]
    enumerations_descriptions: dict[str, str]


def generate_aes_to_oas_enum(aes: RemnawaveAES) -> ErrorEnumEntry:
    enumerations: dict[str, str] = {}
    enumerations_descriptions: dict[str, str] = {}

    for error_name, error in aes.errors.items():
        enumerations[error_name] = error.error_code
        enumerations_descriptions[error_name] = error.message

    return ErrorEnumEntry(
        name="ErrorCode",
        description="Error code of the API.",
        type="string",
        enumerations=enumerations,
        enumerations_descriptions=enumerations_descriptions,
    )


__all__ = ("generate_aes_to_oas_enum",)
