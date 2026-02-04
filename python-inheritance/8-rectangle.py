#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class represents a rectangle defined by its width and height,
and relies on BaseGeometry to validate that its dimensions are positive
integers.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using width and height.

    The width and height are private attributes and must be validated
    as positive integers using the integer_validator method inherited
    from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
