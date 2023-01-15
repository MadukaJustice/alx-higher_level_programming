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

    def to_json(self):
        """
            Retrieves a dictionary representation of a Student instance
        """
        return (self.__dict__)
