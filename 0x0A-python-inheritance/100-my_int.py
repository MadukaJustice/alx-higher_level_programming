#!/usr/bin/python3
"""
    Initialize Module
"""


class MyInt(int):
    """
        Defines a function that reverses the comparison operators
    """
    def __init__(self, value):
        """
            Set initial value
        """
        self.__value = value

    def __eq__(self, value):
        """
            Set value not equal to itself
        """
        return (self.__value != value)

    def __ne__(self, value):
        return (self.__value == value)
