#!/usr/bin/python3
"""
This module defines a custom list class that extends the built-in list.

The class adds a method that allows printing the list elements
in ascending order without modifying the original list.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list type.

    This class provides an additional method to display the elements
    of the list in sorted order while keeping the original list unchanged.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.

        The original list remains unchanged after printing.
        """
        print(sorted(self))
