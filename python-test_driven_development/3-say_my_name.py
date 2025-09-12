#!/usr/bin/python3
"""
This module provides a function that prints a full name
with proper type checking for first and last names.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): First name
        last_name (str): Last name (default is empty string)

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Imprime le nom complet avec un espace final même si last_name est vide
    print("My name is {} {}".format(first_name, last_name))
