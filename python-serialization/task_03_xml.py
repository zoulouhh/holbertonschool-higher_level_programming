#!/usr/bin/python3
"""
Module for serializing and deserializing Python dictionaries to and from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): File path to save the XML.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Path to the XML file.

    Returns:
        dict: Dictionary representation of the XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        
