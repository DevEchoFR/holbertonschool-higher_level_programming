#!/usr/bin/env python3
"""
Module: task_00_basic_serialization
-----------------------------------
This module provides basic JSON serialization and deserialization
functions for Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the JSON file.
    """
    with open(filename, mode="w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and returns it as a dictionary.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, mode="r") as f:
        return json.load(f)
