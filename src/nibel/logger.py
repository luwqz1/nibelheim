from __future__ import annotations

import logging
import re
import sys
import threading
import typing
from contextlib import suppress

import msgspec
import structlog

try:
    import colorama  # type: ignore
except ImportError:
    colorama = None

if typing.TYPE_CHECKING:
    from _typeshed import SupportsWrite

if colorama is not None:
    colorama.just_fix_windows_console()
    colorama.init(wrap=False)

_IS_WIN: typing.Final = sys.platform == "win32"
_LOCK: typing.Final = threading.Lock()
_STRUCTLOG_IS_CONFIGURED: typing.Final = False
_LOGGERS: typing.Final = dict[str, logging.Logger]()
_ALL: typing.Final = "*"

MEGABYTE: typing.Final = 1024**2
ANSI_ESCAPE: typing.Final = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
BRACE_PATTERN: typing.Final = re.compile(r"\{(?:([^}]*?)(?:!([sra]))?)?\}")
HAS_NAMED_PATTERN: typing.Final = re.compile(r"%\([^)]+\)")
HAS_POSITIONAL_PATTERN: typing.Final = re.compile(r"%[sdfrx]")
PERCENT_PATTERN: typing.Final = re.compile(r"%(?:\(([^)]+)\))?([sdfrx])")
STDLIB_PROCESSORS: typing.Final = (
    structlog.contextvars.merge_contextvars,
    structlog.stdlib.filter_by_level,
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
)


class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_WHITE = "\033[97m"
    LIGHT_BLACK = "\033[90m"


class _CallsiteParameterAdder(structlog.processors.CallsiteParameterAdder):
    _handlers = structlog.processors.CallsiteParameterAdder._handlers | {  # type: ignore
        structlog.processors.CallsiteParameter.MODULE: (
            lambda module, frame: frame.f_globals.get("__name__", module)  # type: ignore
        ),
    }


class _LoggerConfig(typing.TypedDict, total=False):
    level: typing.NotRequired[int]
    colors: typing.NotRequired[bool]
    stream: typing.NotRequired[SupportsWrite[str] | None]
    filename: typing.NotRequired[str]
    file_handler: typing.NotRequired[logging.FileHandler]
    json: typing.NotRequired[bool]
    json_indent: typing.NotRequired[int]
    json_serializer: typing.NotRequired[typing.Callable[..., str | bytes]]
    context: typing.NotRequired[dict[str, typing.Any]]


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
    module: str = _ALL,
    /,
    **kwargs: typing.Unpack[_LoggerConfig],
) -> None:
    global _STRUCTLOG_IS_CONFIGURED  # noqa: PLW0603

    with _LOCK:
        if kwargs.get("colors", True) and _IS_WIN and colorama is None:
            raise RuntimeError("Dependency `colorama` is needed to colorize logs on Windows.")

        stream = kwargs.get("stream", sys.stderr)
        colors = False if stream is None else kwargs.get("colors", True)

        handlers: list[logging.Handler] = []
        renderers: list[structlog.types.Processor] = []

        if stream is not None:
            handlers.append(logging.StreamHandler(stream))

        if (filename := kwargs.get("filename")) is not None or (file_handler := kwargs.get("file_handler")) is not None:
            handlers.append(logging.FileHandler(filename) if filename is not None else file_handler)  # type: ignore

        if kwargs.get("json", False):
            renderers.append(
                structlog.processors.JSONRenderer(
                    serializer=kwargs.get("json_serializer", msgspec_json_serializer),
                    indent=kwargs.get("json_indent"),
                ),
            )
        elif stream is not None:
            renderers.append(structlog.dev.ConsoleRenderer(colors=colors))

        for logger in _LOGGERS.values():
            if module != _ALL and not logger.name.startswith(module):
                continue

            logger.setLevel(kwargs.get("level", logging.INFO))

            for handler in handlers:
                if handler.formatter is None:
                    handler.setFormatter(logging.Formatter("%(message)s"))

            logger.handlers.extend(handlers)

        if not _STRUCTLOG_IS_CONFIGURED:
            _STRUCTLOG_IS_CONFIGURED = True  # type: ignore

            structlog.contextvars.clear_contextvars()
            structlog.configure(
                processors=(
                    *STDLIB_PROCESSORS,
                    _SLF4JStyleFormatter(colors=colors),
                    *DEFAULT_PROCESSORS,
                    *renderers,
                ),
                wrapper_class=structlog.stdlib.BoundLogger,
                context_class=dict,
                logger_factory=structlog.stdlib.LoggerFactory(),
                cache_logger_on_first_use=True,
            )

        _ = structlog.contextvars.bind_contextvars(**kwargs.get("context", {}))


def get_logger(name: str, /) -> structlog.stdlib.BoundLogger:
    with _LOCK:
        logger = logging.getLogger(name)

        if name not in _LOGGERS:
            _LOGGERS[name] = logger

    return structlog.wrap_logger(logger)


class _SLF4JStyleFormatter:
    LEVELS_COLORS: typing.Final = {
        "debug": colorama.Fore.LIGHTBLUE_EX if colorama is not None else Colors.LIGHT_BLUE,
        "info": colorama.Fore.LIGHTGREEN_EX if colorama is not None else Colors.LIGHT_GREEN,
        "warning": colorama.Fore.LIGHTYELLOW_EX if colorama is not None else Colors.LIGHT_YELLOW,
        "error": colorama.Fore.LIGHTRED_EX if colorama is not None else Colors.LIGHT_RED,
        "critical": colorama.Fore.LIGHTRED_EX if colorama is not None else Colors.LIGHT_RED,
    }

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
                event_dict["event"], used_kwargs = self._format_braces(
                    event,
                    args,
                    kwargs,
                    log_level,
                )
            elif PERCENT_PATTERN.search(event):
                event_dict["event"], used_kwargs = self._format_percent(
                    event,
                    args,
                    kwargs,
                    log_level,
                )
            elif args:
                event_dict["event"] = self._highlight_values(event, args, log_level)
            else:
                event_dict["event"] = event

        event_dict.pop("positional_args", None)

        for key in used_kwargs:
            event_dict.pop(key, None)

        return event_dict

    def _colorize(self, value: typing.Any, log_level: str) -> str:
        return f"{self.LEVELS_COLORS[log_level]}{value}{colorama.Fore.RESET if colorama is not None else Colors.RESET}" if self.colors else value

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

    def _format_percent(  # noqa: C901, PLR0912
        self,
        message: str,
        args: tuple[typing.Any, ...],
        kwargs: dict[str, typing.Any],
        log_level: str,
    ) -> tuple[str, set[str]]:
        used_kwargs: set[str] = set()

        try:
            has_named = bool(HAS_NAMED_PATTERN.search(message))
            has_positional = bool(HAS_POSITIONAL_PATTERN.search(message))

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
        except TypeError, KeyError, ValueError:
            if kwargs:
                try:
                    formatted = message % kwargs
                    used_kwargs = set(kwargs.keys())
                    for value in kwargs.values():
                        formatted = self._highlight_single_value(formatted, value, log_level)
                    return formatted, used_kwargs
                except TypeError, KeyError:
                    pass

            if args:
                try:
                    formatted = message % args
                    for value in args:
                        formatted = self._highlight_single_value(formatted, value, log_level)
                    return formatted, used_kwargs
                except TypeError, ValueError:
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
