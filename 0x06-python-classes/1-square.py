#!/usr/bin/python3

"""
    Define a new class (Square)
"""


class Square:
    """
    A class that defines a square and initializes a private variable (size)
    """

    def __init__(self, size):
        """
        Initializes a new square

        Attributes:
            size: size of the square
        """
        self.__size = size
