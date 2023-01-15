#!/usr/bin/python3
"""
    Initialize Module
"""


class BaseGeometry():
    """
        Defines base geometry class
    """
    def area(self):
        """
            Raises area exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates 'value' passed
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (int(value) <= 0):
            raise ValueError("{} must be greater than 0".format(name))
