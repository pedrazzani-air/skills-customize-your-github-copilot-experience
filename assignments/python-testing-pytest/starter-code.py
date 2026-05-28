"""Starter functions for the Python Testing with Pytest assignment."""


def calculate_total(price: float, tax_rate: float = 0.1) -> float:
    """Return total price with tax rounded to 2 decimals."""
    return round(price * (1 + tax_rate), 2)


def is_valid_password(password: str) -> bool:
    """Check if password has at least 8 chars and at least one digit."""
    has_min_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    return has_min_length and has_digit


def apply_coupon(total: float, coupon_code: str) -> float:
    """Apply a 10% discount for SAVE10; otherwise return original total."""
    if coupon_code == "SAVE10":
        return round(total * 0.9, 2)
    return total
