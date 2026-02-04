#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

It provides basic methods meant to be extended by other geometry classes.
"""


class BaseGeometry:
    """
    A base class for geometry objects.

    It includes an unimplemented area method and an integer validation method.
    """

    def area(self):
        """
        Raises an exception because area is not implemented in this base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value to validate.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
