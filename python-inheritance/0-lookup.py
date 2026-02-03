#!/usr/bin/python3
"""
This module provides a function to inspect an object.

The function returns a list of all available attributes and
methods of the given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect

    Returns:
        list: A list containing attribute and method names
    """
    return dir(obj)
