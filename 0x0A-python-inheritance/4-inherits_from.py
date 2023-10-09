#!/usr/bin/python3
"""Defines an inherited class checking func."""


def inherits_from(obj, a_class):
    """Checks if an obj is an inherited instance of class.

    Args:
        obj: object to check.
        a_class: class to match type of object.
    Returns: boolean true or false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
