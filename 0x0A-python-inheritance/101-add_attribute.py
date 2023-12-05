#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, fl, num):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        fl (str): The name of the attribute to add to obj.
        num (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, fl, num)
