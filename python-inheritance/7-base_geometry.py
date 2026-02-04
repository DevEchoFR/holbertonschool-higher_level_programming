#!/usr/bin/python3
"""
This module defines a base geometry class.

The class provides methods that can be reused by other
geometry-related classes.
"""


class BaseGeometry:
    """
    A base class for geometric objects.

    This class serves as a foundation for other geometry
    classes and provides common validation methods.
    """

    def area(self):
        """
        Raises an exception indicating that the area
        method has not been implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
