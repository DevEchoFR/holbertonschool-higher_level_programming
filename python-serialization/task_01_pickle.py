#!/usr/bin/env python3
"""
task_01_pickle.py

Pickling Custom Classes:
- Define CustomObject with name, age, is_student
- Provide display(), serialize(), and deserialize()
- On missing/malformed files, return None
"""

import pickle


class CustomObject:
    """A simple custom class that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to `filename`.
        Return None if something goes wrong.
        """
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return a CustomObject from `filename`.
        Return None on errors or wrong content.
        """
        try:
            with open(filename, mode="rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None
            return obj
        except (AttributeError, OSError, pickle.UnpicklingError, EOFError):
            return None
