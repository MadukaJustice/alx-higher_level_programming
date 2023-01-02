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

    def area(self):
        """
            Computes area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Computes perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
            Rectangular pattern
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["#"*self.__width for rows in range(self.__height)]))
