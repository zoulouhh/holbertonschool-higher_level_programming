#!/usr/bin/python3
"""This module is a function to list attributes and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
