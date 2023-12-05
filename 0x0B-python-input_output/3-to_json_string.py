#!/usr/bin/python3
"""Defines a from-JSON-string function."""

import json


def to_json_string(my_obj):
    """Return the JSON string."""
    return json.dumps(my_obj)
