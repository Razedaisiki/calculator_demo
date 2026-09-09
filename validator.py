"""Input validation helpers for the calculator application."""

from exceptions import InvalidNumberError, UnsupportedOperationError

SUPPORTED_OPERATIONS = ("add", "subtract", "multiply", "divide")


def validate_operation(op):
    """Validate that ``op`` is a supported operation name.

    Args:
        op: The operation name to validate.

    Returns:
        The operation name when it is one of the supported operations.

    Raises:
        UnsupportedOperationError: If ``op`` is not a supported operation.
    """
    if op not in SUPPORTED_OPERATIONS:
        raise UnsupportedOperationError(f"Unsupported operation: {op}")
    return op


def parse_number(value):
    """Convert a string to an ``int`` or ``float``.

    Args:
        value: The string value to convert.

    Returns:
        An ``int`` when ``value`` represents an integer, otherwise a ``float``.

    Raises:
        InvalidNumberError: If ``value`` cannot be parsed as a number.
    """
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    try:
        text = str(value).strip()
    except Exception as exc:
        raise InvalidNumberError(f"Invalid number: {value!r}") from exc
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError as exc:
        raise InvalidNumberError(f"Invalid number: {value!r}") from exc
