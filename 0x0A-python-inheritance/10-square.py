#!/usr/bin/python3
"""Defines a Class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle, and initializes size,
    after validating by integer_validator method of the parent class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2
