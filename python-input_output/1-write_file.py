#!/usr/bin/python3
"""
Module 1-write_file
Provides a function to write a string to a UTF-8 text file.
"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
