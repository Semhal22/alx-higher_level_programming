#!/usr/bin/python3
"""Module contains function is_kind_of__class"""


def is_kind_of_class(obj, a_class):
    """Compares if object is an instance of specified class

    Args:
        obj: object to check if instance
        a_class: class
    Returns:
        bool: True if it is and False otherwise
    """
    return isinstance(obj, a_class)
