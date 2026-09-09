"""Tests for the validator helpers defined in validator.py."""

import pytest

import validator
from exceptions import InvalidNumberError, UnsupportedOperationError


@pytest.mark.parametrize("op", ["add", "subtract", "multiply", "divide"])
def test_validate_operation_accepts_supported(op):
    assert validator.validate_operation(op) == op


def test_validate_operation_unsupported_raises():
    with pytest.raises(UnsupportedOperationError):
        validator.validate_operation("power")


def test_parse_number_integer_string():
    assert validator.parse_number("5") == 5


def test_parse_number_negative_decimal_string():
    assert validator.parse_number("-3.2") == pytest.approx(-3.2)


def test_parse_number_invalid_letters_raises():
    with pytest.raises(InvalidNumberError):
        validator.parse_number("abc")


def test_parse_number_empty_string_raises():
    with pytest.raises(InvalidNumberError):
        validator.parse_number("")


def test_parse_number_none_raises():
    with pytest.raises(InvalidNumberError):
        validator.parse_number(None)
