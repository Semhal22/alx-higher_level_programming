#!/usr/bin/python3
"""Module that has one function lookup"""


def lookup(obj):
    """Lookup avaliable methods and atributes of an object

    Args:
        obj: The object

    Returns:
        list: of the attributes and methods
    """
    return dir(obj)
