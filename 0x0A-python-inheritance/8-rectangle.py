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
