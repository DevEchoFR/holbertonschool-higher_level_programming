#!/usr/bin/python3
"""
This module provides a function that checks whether an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class,
        otherwise False.
    """
    return type(obj) is a_class
