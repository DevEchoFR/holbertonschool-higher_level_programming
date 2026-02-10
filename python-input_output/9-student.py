#!/usr/bin/python3
"""
Defines a Student class that can be represented as a dictionary.
"""


class Student:
    """
    Represents a student with basic personal information.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the instance.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
