#!/usr/bin/python3
"""Defines file-writing function."""


def write_file(filename="", text=""):
    """Write a string to my_first_file.txt" file .

    Args:
        filename (str): file name acceptthe path.
        text (str): the write text in file.
    Returns: the len of char in text.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
