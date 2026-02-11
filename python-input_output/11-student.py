#!/usr/bin/python3
"""Defines a Student with JSON-like dict export and reload (no imports)."""


class Student:
    """Represents a student with basic attributes and JSON-style helpers."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            data = {}
            for name in attrs:
                if hasattr(self, name):
                    data[name] = getattr(self, name)
            return data
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
