#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class represents a rectangle defined by its width and height
and provides methods to compute its area and return a string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using width and height.

    This class inherits from BaseGeometry and validates its dimensions
    before storing them as private attributes.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: A formatted string describing the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
