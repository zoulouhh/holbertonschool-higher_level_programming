#!/usr/bin/python3
"""
Module 2-append_write
Provides a function to append a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns number of chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
