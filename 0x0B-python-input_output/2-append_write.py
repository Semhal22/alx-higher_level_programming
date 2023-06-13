#!/usr/bin/python3
"""This module contains the function append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        str: filename
        str: text to append to the file

    Returns:
        int: number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as a_file:
        return a_file.write(text)
