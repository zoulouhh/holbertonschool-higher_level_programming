#!/usr/bin/python3
"""
Executable script using the Python 3 interpreter.

This script defines a function that writes a string to a UTF-8 encoded
text file and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded).

    If the file does not exist, it will be created.
    If the file already exists, its content will be overwritten.