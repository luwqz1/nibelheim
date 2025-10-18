from __future__ import annotations

import logging
import re
import sys
import threading
import types
import typing
from contextlib import suppress

import colorama
import msgspec
import structlog

if typing.TYPE_CHECKING:
    from _typeshed import SupportsWrite

colorama.just_fix_windows_console()
colorama.init()

_LOCK: typing.Final = threading.Lock()
_LOGGERS: typing.Final[dict[str, logging.Logger] | types.MappingProxyType[str, logging.Logger]] = {}

LEVELS_COLORS: typing.Final = dict(
    debug=colorama.Fore.LIGHTBLUE_EX,
    info=colorama.Fore.LIGHTGREEN_EX,
    warning=colorama.Fore.LIGHTYELLOW_EX,
    error=colorama.Fore.LIGHTRED_EX,
    critical=colorama.Fore.LIGHTRED_EX,
)
ANSI_ESCAPE: typing.Final = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
BRACE_PATTERN: typing.Final = re.compile(r"\{(?:([^}]*?)(?:!([sra]))?)?\}")
PERCENT_PATTERN: typing.Final = re.compile(r"%(?:\(([^)]+)\))?([sdfrx])")
STDLIB_PROCESSORS: typing.Final = (
    structlog.contextvars.merge_contextvars,
    structlog.stdlib.filter_by_level,
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
)


class _CallsiteParameterAdder(structlog.processors.CallsiteParameterAdder):
    _handlers = structlog.processors.CallsiteParameterAdder._handlers | {
        structlog.processors.CallsiteParameter.MODULE: lambda module, frame: frame.f_globals.get("__name__", module),  # type: ignore
    }


DEFAULT_PROCESSORS: typing.Final = (
    structlog.processors.format_exc_info,
    structlog.processors.StackInfoRenderer(),
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.UnicodeDecoder(),
    _CallsiteParameterAdder(
        parameters=[
            structlog.processors.CallsiteParameter.FILENAME,
            structlog.processors.CallsiteParameter.MODULE,
            structlog.processors.CallsiteParameter.FUNC_NAME,
            structlog.processors.CallsiteParameter.LINENO,
            structlog.processors.CallsiteParameter.PROCESS,
        ]
    ),
)


def msgspec_json_serializer(
    x: typing.Any,
    *,
    indent: int | None = None,
    default: typing.Callable[[typing.Any], typing.Any],
) -> str:
    result = msgspec.json.encode(x, enc_hook=default)

    if indent is not None:
        result = msgspec.json.format(result, indent=indent)

    return str(result, encoding="utf-8", errors="replace")


def configure(
    *,
    level: int = logging.INFO,
    colors: bool = True,
    stream: SupportsWrite[str] | None = sys.stderr,
    filename: str | None = None,
    file_handler: logging.FileHandler | None = None,
    json: bool = False,
    json_indent: int | None = None,
    json_serializer: typing.Callable[..., str | bytes] = msgspec_json_serializer,
    **context: typing.Any,
) -> None:
    global _LOGGERS

    with _LOCK:
        if not _LOGGERS:
            return

        if json and stream is not None:
            raise ValueError("Cannot use JSON with stream, only with file.")

        handlers: list[logging.Handler] = []
        renderers: list[structlog.types.Processor] = []

        if stream is not None:
            handlers.append(logging.StreamHandler(stream))

        if filename is not None or file_handler is not None:
            handlers.append(logging.FileHandler(filename) if filename is not None else file_handler)  # type: ignore

        if json:
            renderers.append(structlog.processors.JSONRenderer(serializer=json_serializer, indent=json_indent))
        elif stream is not None:
            renderers.append(structlog.dev.ConsoleRenderer(colors=colors))

        for logger in _LOGGERS.values():
            logger.setLevel(level)

            for handler in handlers:
                if handler.formatter is None:
                    handler.setFormatter(logging.Formatter("%(message)s"))

            logger.handlers.extend(handlers)

        _LOGGERS = types.MappingProxyType[str, logging.Logger](mapping={})  # type: ignore

        structlog.contextvars.clear_contextvars()
        _ = structlog.contextvars.bind_contextvars(**context)

        structlog.configure(
            processors=(*STDLIB_PROCESSORS, _SLF4JStyleFormatter(colors=colors), *DEFAULT_PROCESSORS, *renderers),
            wrapper_class=structlog.stdlib.BoundLogger,
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )


def get_logger(name: str, /) -> structlog.stdlib.BoundLogger:
    with _LOCK:
        if isinstance(_LOGGERS, types.MappingProxyType):
            raise LookupError("Cannot get logger after configuration.")

        logger = logging.getLogger(name)

        if name not in _LOGGERS:
            _LOGGERS[name] = logger

    return structlog.wrap_logger(logger)


class _SLF4JStyleFormatter:
    def __init__(self, *, colors: bool = True) -> None:
        self.colors = colors

    def __call__(
        self,
        logger: typing.Any,
        method_name: str,
        event_dict: typing.MutableMapping[str, typing.Any],
    ) -> typing.MutableMapping[str, typing.Any]:
        args = event_dict.get("positional_args", ())
        event = event_dict.pop("event", "")

        if not isinstance(event, str):
            return event_dict

        log_level = event_dict.get("level", "debug")
        system_fields = {"level", "logger", "service", "positional_args"}
        kwargs = {k: v for k, v in event_dict.items() if k not in system_fields}
        used_kwargs: set[str] = set()

        with suppress(TypeError, ValueError, IndexError, KeyError):
            if BRACE_PATTERN.search(event):
                event_dict["event"], used_kwargs = self._format_braces(event, args, kwargs, log_level)
            elif PERCENT_PATTERN.search(event):
                event_dict["event"], used_kwargs = self._format_percent(event, args, kwargs, log_level)
            elif args:
                event_dict["event"] = self._highlight_values(event, args, log_level)
            else:
                event_dict["event"] = event

        event_dict.pop("positional_args", None)

        for key in used_kwargs:
            event_dict.pop(key, None)

        return event_dict

    def _colorize(self, value: typing.Any, log_level: str) -> str:
        return f"{LEVELS_COLORS[log_level]}{value}{colorama.Fore.RESET}" if self.colors else value

    def _format_braces(
        self,
        message: str,
        args: tuple[typing.Any, ...],
        kwargs: dict[str, typing.Any],
        log_level: str,
    ) -> tuple[str, set[str]]:
        result: list[str] = []
        last_end = 0
        arg_index = 0
        used_kwargs: set[str] = set()

        for match in BRACE_PATTERN.finditer(message):
            result.append(message[last_end : match.start()])

            field_name = match.group(1)
            conversion = match.group(2)

            if field_name:
                if field_name in kwargs:
                    value = kwargs[field_name]
                    used_kwargs.add(field_name)
                else:
                    result.append(match.group(0))
                    last_end = match.end()
                    continue
            elif arg_index < len(args):
                value = args[arg_index]
                arg_index += 1
            else:
                result.append(match.group(0))
                last_end = match.end()
                continue

            if conversion == "r":
                formatted_value = repr(value)
            elif conversion == "s":
                formatted_value = str(value)
            elif conversion == "a":
                formatted_value = ascii(value)
            else:
                formatted_value = str(value)

            result.append(self._colorize(formatted_value, log_level))
            last_end = match.end()

        result.append(message[last_end:])
        return "".join(result), used_kwargs

    def _format_percent(
        self,
        message: str,
        args: tuple[typing.Any, ...],
        kwargs: dict[str, typing.Any],
        log_level: str,
    ) -> tuple[str, set[str]]:
        used_kwargs: set[str] = set()

        try:
            has_named = bool(re.search(r"%\([^)]+\)", message))
            has_positional = bool(re.search(r"%[sdfrx]", message))

            if has_named and not has_positional:
                formatted = message % kwargs
                used_kwargs = set(kwargs.keys())
                for value in kwargs.values():
                    formatted = self._highlight_single_value(formatted, value, log_level)
            elif has_positional and not has_named:
                formatted = message % args
                for value in args:
                    formatted = self._highlight_single_value(formatted, value, log_level)
            elif has_named and has_positional:
                temp_formatted = message

                for key, value in kwargs.items():
                    placeholder = f"%({key})s"
                    if placeholder in temp_formatted:
                        used_kwargs.add(key)
                        replacement = self._colorize(str(value), log_level)
                        temp_formatted = temp_formatted.replace(placeholder, replacement)

                if args and "%s" in temp_formatted:
                    temp_formatted = temp_formatted % args
                    for value in args:
                        temp_formatted = self._highlight_single_value(temp_formatted, value, log_level)

                formatted = temp_formatted
            else:
                formatted = message

            return formatted, used_kwargs
        except (TypeError, KeyError, ValueError):
            if kwargs:
                try:
                    formatted = message % kwargs
                    used_kwargs = set(kwargs.keys())
                    for value in kwargs.values():
                        formatted = self._highlight_single_value(formatted, value, log_level)
                    return formatted, used_kwargs
                except (TypeError, KeyError):
                    pass

            if args:
                try:
                    formatted = message % args
                    for value in args:
                        formatted = self._highlight_single_value(formatted, value, log_level)
                    return formatted, used_kwargs
                except (TypeError, ValueError):
                    pass

            return message, used_kwargs

    def _highlight_single_value(
        self,
        message: str,
        value: typing.Any,
        log_level: str,
    ) -> str:
        with suppress(Exception):
            for raw in (str(value), repr(value)):
                if raw in message:
                    pattern = re.compile(rf"(?<!\w){re.escape(raw)}(?!\w)")
                    message = pattern.sub(lambda m: self._colorize(m.group(0), log_level), message, count=1)
                    break

        return message

    def _highlight_values(
        self,
        full_message: str,
        values: typing.Iterable[typing.Any],
        log_level: str,
    ) -> str:
        for value in values:
            full_message = self._highlight_single_value(full_message, value, log_level)
        return full_message


structlog.configure(wrapper_class=structlog.stdlib.BoundLogger)


__all__ = ("configure", "get_logger")
