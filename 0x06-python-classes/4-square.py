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
        self.__size = size

    @property
    def size(self):
        """
            Returns current Square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            Property setter for size attribute
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
            Returns current square area
        """
        return (self.__size**2)
