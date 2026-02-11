#!/usr/bin/python3
"""
This module provides functionality for reading and displaying
the contents of a UTF-8 text file to standard output.

The module does not handle exceptions related to file permissions
or missing files and does not rely on any imported modules.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, mode="r", encoding="utf-8") as text:
        print(text.read(), end="")
