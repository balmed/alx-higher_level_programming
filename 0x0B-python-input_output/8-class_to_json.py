#!/usr/bin/python3
"""Defines the class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure 
    (list, dictionary, string, integer & boolean)."""
    return obj.__dict_
