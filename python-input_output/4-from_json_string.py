#!/usr/bin/python3
"""
Module: JSON to Python Object

This module provides a function that converts a JSON-formatted
string into its corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): A string containing JSON data

    Returns:
        object: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)
