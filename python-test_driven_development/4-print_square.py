#!/usr/bin/python3
"""
Module that defines a function to print a square using the # character.
"""


def print_square(size):
    """
    Prints a square made of # characters.

    Args:
        size (int): length of the square sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """

    if type(size) is bool:
        raise TypeError("size must be an integer")

    if type(size) not in int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
