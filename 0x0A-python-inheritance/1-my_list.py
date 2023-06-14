#!/usr/bin/python3
"""Module contain one class MyList"""


class MyList(list):
    """This class inherits from the list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
