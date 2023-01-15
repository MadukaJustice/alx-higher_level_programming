#!/usr/bin/python3
"""
    Initialize Module
"""


class Student():
    """
        Defines Student() Class
    """

    def __init__(self, first_name, last_name, age):
        """
            Initialization of new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return (self.__dict__)

        new_dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        """
            Replaces all attributes of a Student Instance
        """
        for (key, value) in json.items():
            setattr(self, key, value)
