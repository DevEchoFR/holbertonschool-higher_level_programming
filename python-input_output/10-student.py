#!/usr/bin/python3
"""
Defines a Student class with optional JSON filtering.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.
        """
        if attrs is None:
            return self.__dict__.copy()

        result = {}
        for name in attrs:
            if hasattr(self, name):
                result[name] = getattr(self, name)

        return result
