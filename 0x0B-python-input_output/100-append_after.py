#!/usr/bin/python3
"""Defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename: name of the file.
        search_string: string to search for within the file.
        new_string: string to insert.
    """
    text_content = ""
    with open(filename) as r:
        for l in r:
            text_content += l
            if search_string in l:
                text_content += new_string
    with open(filename, "w") as w:
        w.write(text_content)

