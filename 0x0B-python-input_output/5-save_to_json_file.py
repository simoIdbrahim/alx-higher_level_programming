#!/usr/bin/python3
"""Defines a save-to-json-file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a text file using JSON."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
