#!/usr/bin/python3
"""
Module: append_write
This module provides a function that appends text to a file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): name of the file
        text (str): text to append

    Returns:
        int: number of characters added
    """
    with open(filename, mode="a") as something:
        result = something.write(text)

    return result
