import hashlib
import hmac
import typing

import msgspec

REMNAWAVE_SIGNATURE_HEADER: typing.Final = "x-remnawave-signature"


def validate_webhook_signature(
    body: typing.Any,
    signature: str | bytes,
    secret: str | bytes,
    /,
) -> bool:
    if not isinstance(body, (str, bytes)):
        body = msgspec.json.encode(body)

    if isinstance(signature, bytes):
        signature = signature.decode("UTF-8")

    computed_signature = hmac.new(
        secret.encode("UTF-8") if isinstance(secret, str) else secret,
        body.encode("UTF-8") if isinstance(body, str) else body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(computed_signature, signature)


def validate_webhook_signature_from_headers(
    body: typing.Any,
    headers: typing.Mapping[str | bytes, str | bytes],
    secret: str | bytes,
    /,
) -> bool:
    header_str = REMNAWAVE_SIGNATURE_HEADER
    header_bytes = REMNAWAVE_SIGNATURE_HEADER.encode("UTF-8")

    if not (
        signature := next(
            (v for k, v in headers.items() if (k.lower() if isinstance(k, str) else k.lower()) == (header_str if isinstance(k, str) else header_bytes)),
            None,
        )
    ):
        return False

    return validate_webhook_signature(body, signature, secret)


__all__ = ("validate_webhook_signature", "validate_webhook_signature_from_headers")
