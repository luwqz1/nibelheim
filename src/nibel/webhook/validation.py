import hashlib
import hmac
import typing

import msgspec

REMNAWAVE_SIGNATURE_HEADER: typing.Final = "x-remnawave-signature"


def validate_webhook_signature(
    body: typing.Any,
    signature: str,
    secret: str,
    /,
) -> bool:
    if not isinstance(body, (str, bytes)):
        body = msgspec.json.encode(body)

    computed_signature = hmac.new(
        secret.encode("UTF-8"),
        body.encode("UTF-8") if isinstance(body, str) else body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(computed_signature, signature)


def validate_webhook_headers(
    body: typing.Any,
    headers: typing.Mapping[str, str],
    secret: str,
    /,
) -> bool:
    if not (
        signature := next(
            (v for k, v in headers.items() if k.lower() == REMNAWAVE_SIGNATURE_HEADER.lower()),
            None,
        )
    ):
        return False

    return validate_webhook_signature(body, signature, secret)


__all__ = ("validate_webhook_headers", "validate_webhook_signature")
