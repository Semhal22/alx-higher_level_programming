#!/usr/bin/python3
"""Module contains class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square by calling super class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns printed text"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
