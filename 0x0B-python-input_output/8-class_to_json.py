#!/usr/bin/python3
"""
    Initialize Module
"""


def class_to_json(obj):
    """
        Retursn the dictionary description with simple data structure
        for JSON serialization of an object
    """
    return (obj.__dict__)
