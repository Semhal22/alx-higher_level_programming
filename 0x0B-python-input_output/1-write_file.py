#!/usr/bin/python3
"""This module contains the function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        str: filename
        str: text to write to the file

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        return a_file.write(text)
