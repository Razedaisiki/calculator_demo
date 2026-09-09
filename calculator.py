"""Command line interface entry point for the calculator application."""

import sys

import operations
import validator
from exceptions import (
    DivisionByZeroError,
    InvalidNumberError,
    UnsupportedOperationError,
)


OPERATION_DISPATCH = {
    "add": operations.add,
    "subtract": operations.subtract,
    "multiply": operations.multiply,
    "divide": operations.divide,
}


def main(argv):
    """Run the calculator CLI.

    Args:
        argv: The full ``sys.argv`` list. ``argv[1]`` is the operation name
            and ``argv[2]``/``argv[3]`` are the numeric operands.

    Returns:
        An integer exit code: ``0`` on success, non-zero on error.
    """
    try:
        op = validator.validate_operation(argv[1])
    except UnsupportedOperationError:
        print("Error: unsupported operation")
        return 1

    try:
        a = validator.parse_number(argv[2])
        b = validator.parse_number(argv[3])
    except InvalidNumberError:
        print("Error: invalid number")
        return 1

    try:
        result = OPERATION_DISPATCH[op](a, b)
    except DivisionByZeroError:
        print("Error: cannot divide by zero")
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
