#!/usr/bin/python3
"""
This module provides a function to verify the exact class of an object.

The function checks whether an object is created directly
from a specified class, without considering inheritance.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check
        a_class (type): The class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False
    """
    obj_class = type(obj)

    if obj_class == a_class:
        return True
    else:
        return False
