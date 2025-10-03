#!/usr/bin/python3
"""
Basic Serialization Module

Provides functions to serialize a Python dictionary
to a JSON file and deserialize it back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    If the file already exists, it will be overwritten.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Path to the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Path to the input JSON file

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
