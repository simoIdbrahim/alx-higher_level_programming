#!/usr/bin/python3
"""Defines load-from-json-file function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as file:
        return json.load(file)
