#!/usr/bin/python3
"""Defines a square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes a square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size
