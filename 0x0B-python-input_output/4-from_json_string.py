#!/usr/bin/python3
"""Module contains function from_json_string and also imports json"""
import json


def from_json_string(my_str):
    """Converts JSON representation to obj

    Returns:
        object: Python data structure
    """
    return json.loads(my_str)
