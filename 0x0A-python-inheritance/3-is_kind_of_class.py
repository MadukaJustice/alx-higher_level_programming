#!/usr/bin/python3
"""
    Initialize Module
"""


def is_kind_of_class(obj, a_class):
    """
        Checks if an object is an instance of the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
