#!/usr/bin/python3
"""Defines func that adds att to objs."""


def add_attribute(obj, att, value):
    """Add a new attribute to an obj if possible.

    Args:
        obj: object to add an attribute to.
        att: name of attribute to add to obj.
        value: value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
