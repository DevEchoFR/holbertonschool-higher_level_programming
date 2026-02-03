#!/usr/bin/python3
"""
This module defines a custom list class.

The MyList class extends the built-in list type and
adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList inherits from the built-in list class.

    It provides an additional method to display
    the list elements sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        The original list must NOT be modified.
        All elements are assumed to be integers.
        """

        # Step 1: Create a copy of the current list
        copied_list = self.copy()

        # Step 2: Sort the copied list
        copied_list.sort()

        # Step 3: Print the sorted list
        print(copied_list)
