#!/usr/bin/env python3
"""
task_03_xml.py

Provides functions to serialize a Python dictionary into XML
and deserialize XML back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a dictionary.
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for element in root:
        result[element.tag] = element.text

    return result
