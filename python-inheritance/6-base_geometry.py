#!/usr/bin/python3
"""Basic model for creating shapes.
    Setting up a space where we can calculate their sizes later."""


class BaseGeometry:
    """A starting point for all shapes."""

    def area(self):
        """Try to find the shape's size.

        Raises:
            Exception: Always says "We don't know how to calculate this yet!"
        """
        raise Exception("area() is not implemented")
