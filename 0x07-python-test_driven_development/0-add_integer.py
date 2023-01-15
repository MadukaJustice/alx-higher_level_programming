#!/usr/bin/python3
"""
    Initialize function which adds two integers
"""


def add_integer(a, b=98):
    """
        Returns sum of int(a) and int(b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
