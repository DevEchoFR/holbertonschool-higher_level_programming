#!/usr/bin/python3
"""
Module that loads a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename, mode="r") as f:
        return json.load(f)
