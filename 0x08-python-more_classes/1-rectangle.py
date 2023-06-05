#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Rectangle with private instance attributes width and height"""
    def __init__(self, width=0, height=0):
        """"Instantiate width and height
        Args:
            width: of rectangle
            height: of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function
        Returns: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to set the width
        Args:
            value: width of rectangle to be set
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function to set the width
        Args:
            value: height to be set
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
