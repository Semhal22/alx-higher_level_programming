#!/usr/bin/python3
"""Module contains function to_json_string and also imports json"""
import json


def to_json_string(my_obj):
    """Converts an object to its JSON representation

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
