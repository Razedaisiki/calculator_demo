"""End-to-end CLI tests that exercise calculator.py as a real subprocess.

These tests invoke ``calculator.py`` via ``subprocess.run`` so the full CLI
behavior is validated, including argument parsing, stdout/stderr output, and
process exit codes. They also verify that error paths do not leak Python
tracebacks to stderr.
"""

import os
import subprocess
import sys

import pytest


# Path to the calculator script. ``__file__`` lives in ``tests/`` so we
# resolve one directory up to reach the project root.
CALCULATOR_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "calculator.py"
)


def _run_calculator(*args):
    """Invoke ``calculator.py`` with ``args`` and return the completed process.

    Returns:
        subprocess.CompletedProcess: The finished process with captured
        ``stdout``, ``stderr``, and ``returncode``.
    """
    return subprocess.run(
        [sys.executable, CALCULATOR_PATH, *args],
        capture_output=True,
        text=True,
    )


# ---------------------------------------------------------------------------
# Happy path tests
# ---------------------------------------------------------------------------


def test_cli_add_produces_correct_result():
    result = _run_calculator("add", "10", "5")
    assert result.returncode == 0
    assert result.stdout.strip() == "15"
    assert result.stderr == ""


def test_cli_subtract_produces_correct_result():
    result = _run_calculator("subtract", "10", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "7"
    assert result.stderr == ""


def test_cli_multiply_produces_correct_result():
    result = _run_calculator("multiply", "4", "6")
    assert result.returncode == 0
    assert result.stdout.strip() == "24"
    assert result.stderr == ""


def test_cli_divide_produces_correct_result():
    result = _run_calculator("divide", "20", "4")
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"
    assert result.stderr == ""


# ---------------------------------------------------------------------------
# Error path tests
# ---------------------------------------------------------------------------


def test_cli_unsupported_operation_prints_error_and_exits_nonzero():
    result = _run_calculator("power", "2", "3")
    assert result.returncode != 0
    assert "Error: unsupported operation" in result.stdout
    # No Python traceback should leak to stderr.
    assert "Traceback" not in result.stderr
    assert result.stderr == ""


def test_cli_invalid_number_prints_error_and_exits_nonzero():
    result = _run_calculator("add", "abc", "3")
    assert result.returncode != 0
    assert "Error: invalid number" in result.stdout
    assert "Traceback" not in result.stderr
    assert result.stderr == ""


def test_cli_division_by_zero_prints_error_and_exits_nonzero():
    result = _run_calculator("divide", "10", "0")
    assert result.returncode != 0
    assert "Error: cannot divide by zero" in result.stdout
    assert "Traceback" not in result.stderr
    assert result.stderr == ""


# ---------------------------------------------------------------------------
# Parametrized exact-string assertions to lock the documented error messages
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "args, expected_message",
    [
        (("power", "2", "3"), "Error: unsupported operation"),
        (("add", "abc", "3"), "Error: invalid number"),
        (("divide", "10", "0"), "Error: cannot divide by zero"),
    ],
)
def test_cli_error_messages_are_exact(args, expected_message):
    result = _run_calculator(*args)
    assert result.returncode != 0
    # Trim to ignore any trailing newline from ``print``.
    assert result.stdout.strip() == expected_message
    assert "Traceback" not in result.stderr
    assert "Traceback (most recent call last)" not in result.stderr
    assert result.stderr == ""
