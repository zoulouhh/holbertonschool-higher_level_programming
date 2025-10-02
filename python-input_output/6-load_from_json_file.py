#!/usr/bin/python3
"""
Module 6-load_from_json_file
Provides a function that creates an object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)