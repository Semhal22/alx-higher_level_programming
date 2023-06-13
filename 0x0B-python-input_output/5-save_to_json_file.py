#!/usr/bin/python3
"""This module imports json and contains the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation

    Args:
        obj: can be list, dict
        str: name of file
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
