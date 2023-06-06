#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Rectangle with private instance attributes width and height
    Class attribute number_of_instances to keep count of instances
    Class attribute print_symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """"Instantiate width and height
        Args:
            width: of rectangle
            height: of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rows = [str(self.print_symbol) * self.width
                for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Displays message when object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles interms of area
        Returns: the biggest rectangle
        Raises:
            TypeError: if one of the rectangles is not an
            instance of Rectangle class
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Define a constructor for Rectangle
        Args:
            size: value of both height and width
        Returns: a new instance
        """
        return cls(size, size)
