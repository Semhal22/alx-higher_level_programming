#!/usr/bin/python3
""" Contains a function add_integer """


def add_integer(a, b=98):
    """
    Adds two integers(casted to integers if floats)
    Exceptions:
    TypeError: if a and b are not integers or floats
    Return: an integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
