#!/usr/bin/python3
"""
    Instantiate Class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Defines a Rectangle child class of BaseGeometry parent class
    """
    def __init__(self, width, height):
        """
            Defines the init params of the Rectangle class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        __get = (self.__class__.__name__)
        return ("[{}] {}/{}".format(__get, self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)
