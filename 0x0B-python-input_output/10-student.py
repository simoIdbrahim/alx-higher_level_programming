#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary of the Student.

        If attrs is a list of strings, represents only those attributes
        included in list.

        Args:
            attrs: attributes to represent.
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
