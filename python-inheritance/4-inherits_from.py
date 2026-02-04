#!/usr/bin/python3
"""
This module provides a function that checks whether an object
is an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    directly or indirectly from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare inheritance against.

    Returns:
        bool: True if the object inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
