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

    def my_print(self):
        """
            Prints # square times
        """

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")

    def __str__(self):
        """
            Define the print() representation of a Square instance
        """
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
