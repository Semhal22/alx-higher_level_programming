#!/usr/bin/python3
"""Module contains function is_same_class"""


def is_same_class(obj, a_class):
    """Compares if object is exactly an instance of specified class

    Args:
        obj: object to check if instance
        a_class: class
    Returns:
        bool: True if it is and False otherwise
    """
    return isinstance(obj, a_class)
