#!/usr/bin/python3
"""Module for the BaseGeometry class."""


class BaseGeometry:
    """A basic class for geometric shapes."""

    def area(self):
        """Raise an exception because area is not defined yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if a value is a valid positive integer.

        Args:
            name (str): The name of the value (for error messages).
            value: The value to check.

        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is 0 or less.
        """
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
