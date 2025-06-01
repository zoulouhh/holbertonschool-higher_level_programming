#!/usr/bin/python3
"""This module has a function to check what type of thing an object is."""


def is_kind_of_class(obj, a_class):
    """
    Checks if something is a specific type or related to it.

    Args:
        obj: The thing we're curious about.
        a_class: The type we're wondering about.

    Return:
        True if it's that type or in the family, False if not.
    """
    return isinstance(obj, a_class)
