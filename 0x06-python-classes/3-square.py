#!/usr/bin/python3

"""
    Defines a class Square with private attribute
"""


class Square:
    """
        Definition with __init__ size
    """

    def __init__(self, size=0):
        """
            Initialize Square class

            Attributes:
                size: size of the square of type int
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Returns current square area
        """
        return (self.__size**2)
