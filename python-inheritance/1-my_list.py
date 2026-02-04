#!/usr/bin/python3
"""
This module defines a custom list class that adds a method to print the
elements in ascending order without modifying the original list.
"""


class MyList(list):
    """
    Represents a list of integers with a method to display a sorted version.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without changing the list.
        """
        print(sorted(self))
