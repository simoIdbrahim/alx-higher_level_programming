#!/usr/bin/python3
"""Defines class-checking func."""


def is_same_class(obj, a_class):
    """Check if an object is exactly instance of given class.

    Args:
        obj: check.
        a_class: The class to match the type of object.
    Returns: boolean value true || false
    """
    if type(obj) == a_class:
        return True
    return False

