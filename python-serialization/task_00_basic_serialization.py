#!/usr/bin/env python3


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary into JSON and saves it to a file.
    If the file already exists, it will be replaced
    """
    if not isinstance(data, dict):
        raise TypeError("The 'data' parameter must be a dictionary.")

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to recreate a Python dictionary"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)