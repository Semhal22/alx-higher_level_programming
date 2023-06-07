#!/usr/bin/python3


class LockedClass:
    """Defines slots to be used in this class
    Creation of other attributes raises an AttributeError
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
