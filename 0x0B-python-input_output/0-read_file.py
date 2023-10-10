#!/usr/bin/python3
"""Defines a text file-reading."""


def read_file(filename=""):
    """Print the content of my_file_0.txt file ."""
    read_file_UTF8 = open(filename)
    print(read_file_UTF8.read())
