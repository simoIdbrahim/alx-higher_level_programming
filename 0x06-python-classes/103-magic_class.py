#!/usr/bin/python3
"""MagicClass class."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """constructor function.

        Arg:
            radius: radius new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return: area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return: circumference."""
        return (2 * math.pi * self.__radius)

