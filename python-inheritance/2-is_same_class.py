#!/usr/bin/python3
"""This module contains a function to check the type of an object."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly the requested type.

    Args:
        obj: The object we want to verify.
        a_class: The type we're looking for.

    Return:
        True if it's exactly the right type, False otherwise.
    """
    return type(obj) is a_class
