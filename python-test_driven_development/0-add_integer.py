#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It handles basic types (int, float) and raises errors for invalid types.
"""


def add_integer(a, b=98):
    """
    Return the sum of a plus b.

    :param a: First number
    :type a: int or float
    :param b: Second number
    :type b: int or float
    :return: The addition of a and b
    :rtype: int
    :raises TypeError: If a or b are not integers or floats
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return a + b
