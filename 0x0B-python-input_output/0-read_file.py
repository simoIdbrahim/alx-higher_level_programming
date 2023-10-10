#!/usr/bin/python3
"""Defines a text file-reading."""


def read_file(filename=""):
    """Print the content of my_file_0.txt file ."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
