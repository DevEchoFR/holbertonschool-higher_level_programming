#!/usr/bin/python3
"""
Module: file_writer
This module provides functionality to write text to a file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): name of the file
        text (str): text to write

    Returns:
        int: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
