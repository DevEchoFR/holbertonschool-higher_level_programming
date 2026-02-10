#!/usr/bin/python3
"""Module: Convert a class instance into a JSON-ready dictionary.

This module defines a helper function that returns a dictionary of an
object's serializable attributes (str, int, bool, list, dict).
"""


def class_to_json(obj):
    """Return a dictionary description of obj for JSON serialization."""
    data = obj.__dict__

    return data
