#!/usr/bin/python3
""" Contains function print_squre """


def print_square(size):
    """
    Prints a square with the character #
    Args:
        size: length of the square
    Exceptions:
        TypeError: if size is not an integer or
                    if size is less than 0 and float
        ValueError: size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
