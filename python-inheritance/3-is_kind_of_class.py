#!/usr/bin/python3
"""
This module provides a function that checks whether an object
is an instance of a specified class or a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or an instance
    of a class that inherited from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of the class or
        a subclass of it, otherwise False.
    """
    return isinstance(obj, a_class)
