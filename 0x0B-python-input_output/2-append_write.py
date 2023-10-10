#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of text file.

    Args:
        filename: The name of the file.
        text: The content of the text append.
    Returns: The number of characters appended.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
