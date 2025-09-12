#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function handles both integers and floats.
If a float is provided, it is cast to an integer before addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting floats to integers.

    Args:
        a: first number (int or float).
        b: second number (int or float, default = 98).

    Returns:
        int: the sum of a and b.

    Raises:
        TypeError: if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    