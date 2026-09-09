"""Tests for the arithmetic operations defined in operations.py."""

import pytest

import operations
from exceptions import DivisionByZeroError


def test_add_positive_integers():
    assert operations.add(2, 3) == 5


def test_add_negative_and_float():
    assert operations.add(-4, 2.5) == -1.5


def test_subtract_positive_integers():
    assert operations.subtract(10, 3) == 7


def test_subtract_negative_result():
    assert operations.subtract(3, 10) == -7


def test_subtract_floats():
    assert operations.subtract(5.5, 2.0) == pytest.approx(3.5)


def test_multiply_positive_integers():
    assert operations.multiply(4, 5) == 20


def test_multiply_negative_and_float():
    assert operations.multiply(-3, 2.5) == -7.5


def test_multiply_by_zero():
    assert operations.multiply(7, 0) == 0


def test_divide_valid_integers():
    assert operations.divide(10, 2) == 5


def test_divide_negative_and_float():
    assert operations.divide(-9.0, 2.0) == pytest.approx(-4.5)


def test_divide_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        operations.divide(10, 0)
