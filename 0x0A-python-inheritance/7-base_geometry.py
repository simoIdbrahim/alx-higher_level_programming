#!/usr/bin/python3
"""Defines base geometry cls BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as an int.

        Args:
            name: name of parameter.
            value: parameter to validate.
        Raises:
            TypeError: If val is not an int.
            ValueError: If val is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
