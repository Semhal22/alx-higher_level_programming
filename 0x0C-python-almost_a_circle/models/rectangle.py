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
        """Sets width"""
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height"""
        self.__height = height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x"""
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""
        self.__y = y
