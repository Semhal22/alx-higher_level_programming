#!/usr/bin/python3
"""Module contains a class named BaseGeometry"""


class BaseGeometry:
    """Lays foundation for a basic geometry calculations"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be a correct input"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
