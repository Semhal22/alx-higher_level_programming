#!/usr/bin/python3
""""Module contains a class named Base"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes id with passed id if not None
        Else increments __nb_objects and assigns id

        Args:
            int: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of argument
        Args:
            dict: list_dictionaries
        Returns:
            str: json representation
        """
        if not list_dictionaries:
            return "[]"
        json_repr = json.dumps(list_dictionaries)
        return json_repr
