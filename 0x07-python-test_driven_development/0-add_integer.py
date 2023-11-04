#!/usr/bin/python3
""" Contains a function add_integer """


def add_integer(a, b=98):
    """
    Adds two integers(casted to integers if floats)
    Exceptions:
    TypeError: if a and b are not integers or floats
    Return: an integer
    """
    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
