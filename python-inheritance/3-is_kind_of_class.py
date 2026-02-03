#!/usr/bin/python3
"""
Module: class relationship checker
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class
    or an instance of a class that inherited from it.
    """
    return isinstance(obj, a_class)
