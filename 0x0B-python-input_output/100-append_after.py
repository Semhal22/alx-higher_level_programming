#!/usr/bin/python3
"""Module containing function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Searches for a string and appends new_string after it
    Args:
        filename: name of file
        search_string: string to be searched
        new_string: string to append
    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
