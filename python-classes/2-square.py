#!/usr/bin/python3
"""Defines a square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        # Step 1: Check the TYPE
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Step 2: Check the VALUE
        if size < 0:
            raise ValueError("size must be >= 0")

        # Step 3: Store the value privately
        self.__size = size
