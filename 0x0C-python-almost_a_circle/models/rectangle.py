#!/usr/bin/python3
"""Module that contains a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define the Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle
        Args:
            int: width
            int: height
            int: x
            int: y
            int: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width
        Args:
            int: width
        Exceptions:
            TypeError: if width is not int
            ValueError: if width not greater than 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height
        Args:
            int: height
        Exceptions:
            TypeError: if height is not int
            ValueError: if height is not greater than 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x
        Args:
             int: x
        Exceptions:
            TypeError: if not integer
            ValueError: x under 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y
        Args:
            int: y
        Exceptions:
            TypeError: if not integer
            ValueError: if under 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate Area of Rectangle
        Return:
            int: area
        """
        return self.width * self.height

    def display(self):
        """Print Rectangle with character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns printed text"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"
