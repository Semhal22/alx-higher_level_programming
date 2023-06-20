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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []
        my_dict = [obj.to_dictionary() for obj in list_objs]
        json_repr = cls.to_json_string(my_dict)
        with open(filename, "w", encoding="utf-8") as a_file:
            a_file.write(json_repr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation"""
        if not json_string:
            return []
        my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as a_file:
                json_str = a_file.read()
                list_dicts = cls.from_json_string(json_str)
                list_instances = [cls.create(**d) for d in list_dicts]
                return list_instances
        except FileNotFoundError:
            return []
