#!/usr/bin/python3
def lookup(obj):
    """Lookup avaliable methods and atributes of an object
    Args:
        obj: The object
    Return:
        list: of the attributes and methods
    """
    return dir(obj)
