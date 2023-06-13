#!/usr/bin/python3
"""This module imports json and contains the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a  JSON file

    Args:
        str: name of file

    Returns:
        obj: obj from the json file
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
