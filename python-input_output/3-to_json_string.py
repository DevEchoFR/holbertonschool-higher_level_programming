#!/usr/bin/python3
"""
Module: to_json_string

This module provides a function that converts a Python object
into its JSON string representation.
"""

import json  # ← import the correct standard module


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
