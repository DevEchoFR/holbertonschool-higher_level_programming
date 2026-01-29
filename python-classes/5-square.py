#!/usr/bin/python3
"""Defines a Square class that can be printed."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        # Use the setter here (do NOT assign directly)
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #."""
        if self.__size == 0:
            print()
        else:
            for integer in range(self.__size):
                print("#" * self.__size)
