#!/usr/bin/python3
"""
This module helps discover everything an object can do.
"""


def lookup(obj):
    """
    This function looks at an object and tells you what it can do.
    Args:
    Any Python object you want to know more about.
    Return:
    A list of all the object's abilities and properties
    """
    return dir(obj)
