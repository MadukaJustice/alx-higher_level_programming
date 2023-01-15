#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle():
    """
    Initialize Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
            Initial Params
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Property setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            Property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Property setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
