#!/usr/bin/python3

"""
    Defines a class Square with private attribute
"""


class Square:
    """
        Definition with __init__ size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Initialize Square class

            Attributes:
                size: size of the square of type int
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
            Property definition for position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
            Setter for position attribute
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1])
                is not int or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
            Returns current square area
        """
        return (self.__size**2)

    def __eq__(self, other):
        """
            Compares and returns if equal
        """
        return self.size == other.size

    def __ne__(self, other):
        """
            Compares and returns if not equal
        """
        return self.size != other.size

    def __lt__(self, other):
        """
            Compares and returns if lesser than
        """
        return self.size < other.size

    def __le__(self, other):
        """
            Compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
            Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
            Compares and returns if greater than or equal to
        """
        return self.size >= other.size
