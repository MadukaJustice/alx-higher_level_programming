#!/usr/bin/python3
"""
    Initialize Module
"""


def inherits_from(obj, a_class):
    """
        Checks if an object is an instance of the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
