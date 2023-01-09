#!/usr/bin/python3
"""
    Instantiate Class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Defines a Square child class of Rectangle parent class
    """
    def __init__(self, size):
        """
            Defines the init params of the Square class
        """
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        __get = (self.__class__.__name__)
        return ("[{}] {}/{}".format(__get, self.__size, self.__size))

    def area(self):
        return (self.__size ** 2)
