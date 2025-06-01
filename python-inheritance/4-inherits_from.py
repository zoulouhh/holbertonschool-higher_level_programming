#!/usr/bin/python3
"""This module checks if something comes from a specific family of types."""


def inherits_from(obj, a_class):
    """
    Checks if something is a distant relative of a type.

    Args:
        obj: The thing we're investigating.
        a_class: The type family we're tracing.

    Return:
        True if it's a descendant, False if not.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
