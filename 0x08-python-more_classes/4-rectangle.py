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

    def area(self):
        """Calculates the rectangle area
        Returns: area
        """
        return self.width * self.height

    def check_zero(self):
        """Checks if height or width is 0
        Returns: True if 0 is present
        """
        if (self.height == 0) or (self.width == 0):
            return True

    def perimeter(self):
        """Calculates perimeter of triangle
        Returns: perimeter or 0 if height or width is 0
        """
        if self.check_zero is True:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """Returns the rectangle to be printed with character #
        Returns: or empty string if height or width is 0
        """
        if self.check_zero() is True:
            return ""
        rows = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"
