#!/usr/bin/python3
"""Adds a new attribute to an object if it's possible
or raises a TypeError if not"""


def add_attribute(obj, attr, value):
    """Function that adds a new attribute to an object"""
    if type(obj) in [int, float, list, dict, str, bool]:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
