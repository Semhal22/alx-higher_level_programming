"""Module contains one function class_to_json"""


def class_to_json(obj):
    """Find dictionary description for JSON serialization

    Args:
        obj: instance of a Class

    Returns:
        dict: description of the object
    """
    dictionary = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dictionary[key] = value
    return dictionary
