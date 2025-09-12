#!/usr/bin/python3
"""
This module provides a function that prints a square
using the character #, with proper type and value checks.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)