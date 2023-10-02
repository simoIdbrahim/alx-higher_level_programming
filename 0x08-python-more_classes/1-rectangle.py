#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """rectangle."""

    def __init__(self, width=0, height=0):
        """construction new Rectangle.

        Args:
            width: the width the new rectangle.
            height: the height the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
