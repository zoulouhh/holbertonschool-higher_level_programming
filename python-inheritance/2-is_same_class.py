#!/usr/bin/python3
"""This module defines a function that checks for exact class match."""

def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) == a_class
    
