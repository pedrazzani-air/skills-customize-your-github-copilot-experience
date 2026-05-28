"""Pytest starter file.

Run with:
    pytest
"""

import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).with_name("starter-code.py")
_SPEC = importlib.util.spec_from_file_location("starter_code", _MODULE_PATH)
_MODULE = importlib.util.module_from_spec(_SPEC)
assert _SPEC and _SPEC.loader
_SPEC.loader.exec_module(_MODULE)

apply_coupon = _MODULE.apply_coupon
calculate_total = _MODULE.calculate_total
is_valid_password = _MODULE.is_valid_password


def test_calculate_total_default_tax():
    # TODO: Replace with your own expected value if needed.
    assert calculate_total(100) == 110.0


def test_calculate_total_custom_tax():
    # TODO: Add another scenario with a custom tax.
    assert calculate_total(50, 0.2) == 60.0


def test_is_valid_password_true():
    # TODO: Use another valid password example.
    assert is_valid_password("abc12345") is True


def test_is_valid_password_false():
    # TODO: Use another invalid password example.
    assert is_valid_password("abcdefg") is False


def test_apply_coupon_valid_code():
    # TODO: Check that SAVE10 applies a discount.
    assert apply_coupon(100, "SAVE10") == 90.0


def test_apply_coupon_invalid_code():
    # TODO: Check that unknown coupon codes do not change total.
    assert apply_coupon(100, "NOPE") == 100
