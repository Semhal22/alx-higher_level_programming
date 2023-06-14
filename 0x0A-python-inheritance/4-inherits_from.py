#!/usr/bin/python3
"""Module contains function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class that is inherited

    Args:
        obj: object to check if instance
        a_class: class
    Returns:
        bool: True if it is and False otherwise
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
