#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class with a private instance attribute"""
    def __init__(self, size=0):
        """
        Instantiate size attribute and Raise an error
        if size is not an integer or is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
