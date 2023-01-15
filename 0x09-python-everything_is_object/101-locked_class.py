#!/usr/bin/python3
"""
    Defines a LockedClass
"""


class LockedClass:
    """
        Prevent the user from instantiating new LockedClass attributes
        dynamically unless attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
