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

    def update(self, *args, **kwargs):
        """Updates attributes of Square
        Args:
            list: args(list of arguments)
            dictionary: key/value arguments
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dicitonary representation of the square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
