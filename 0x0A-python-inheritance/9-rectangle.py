#!/usr/bin/python3
"""Module contains a class named Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry, and initializes width and height,
    after validating by integer_validator method of the parent class
    Also the area() method is updated here
    """
    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns text below if str() method is called"""
        return f"[Rectangle] {self.__width}/{self.__height}"
