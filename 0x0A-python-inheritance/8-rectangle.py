#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize new Rectangle.

        Args:
            width: width of new Rectangle.
            height: height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
