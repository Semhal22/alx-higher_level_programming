#!/usr/bin/python3
"""Module contains one function read_file"""


def read_file(filename=""):
    """Reads a text file and prints it

    Args:
        str: filename
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
