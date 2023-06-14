#!/usr/bin/python3
"""Module contains Class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation function
        Args:
            str: first name
            str: last name
            int: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of Student instance

        Returns:
            dictionary
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                dictionary[key] = value
        return dictionary
