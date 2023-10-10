#!/usr/bin/python3
"""Defines a from-json-string function."""
import json


def from_json_string(my_str):
    """Return the Python obj of a JSON string."""
    return json.loads(my_str)
