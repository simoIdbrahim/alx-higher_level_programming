#!/usr/bin/python3
"""Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """constructor function.

        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
