#!/usr/bin/python3
"""
This module defines a custom list class that extends the built-in list
and provides a method to display its elements in sorted order.
"""


class MyList(list):
    """
    Represents a list of integers with an additional method to print
    the elements in ascending sorted order without modifying the list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order without modifying
        the original list.
        """

        print(sorted(self))
