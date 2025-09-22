#!/usr/bin/python3
"""Module that defines the Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle.

        Args:
            width (int): The width of the rectangle (must be positive integer).
            height (int): The height of the rectangle (must be positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
