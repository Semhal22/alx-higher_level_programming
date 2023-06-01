#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class with a private instance attribute
    with a method that uses this attribute
    """
    def __init__(self, size=0):
        """Instantiate size attribute"""
        self.__size = size

    @property
    def size(self):
        """A getter function that returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size, but raises an error if
        size is not an integer or is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Uses the size to return the square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
