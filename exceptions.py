"""Custom exception definitions for the calculator application."""


class UnsupportedOperationError(Exception):
    """Raised when the requested operation is not supported."""


class InvalidNumberError(Exception):
    """Raised when a provided input is not a valid number."""


class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""
