#!/usr/bin/python3
"""1-square.py"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """
        Initializes the Square instance with a given size.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
