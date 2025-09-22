#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Raises an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
