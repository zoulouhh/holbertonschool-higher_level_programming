#!/usr/bin/python3
"""This module defines a function to check class inheritance."""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    from the specified class. Return False if obj is an instance of a_class itself.

    Example:
    >>> class A:
    ...     pass
    >>> class B(A):
    ...     pass
    >>> b = B()
    >>> inherits_from(b, A)
    True
    >>> a = A()
    >>> inherits_from(a, A)
    False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
