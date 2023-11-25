#!/usr/bin/python3
"""Function named text_indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Exceptions:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = False
    for c in text:
        if new_line and c == " ":
            continue
        print(c, end="")
        if c in ['.', '?', ':']:
            print()
            print()
            new_line = True
        else:
            new_line = False
