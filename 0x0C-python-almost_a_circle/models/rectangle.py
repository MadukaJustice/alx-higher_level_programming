#!/usr/bin/python3
"""
    Rectangle class Module
"""


from models.base import Base


class Rectangle(Base):
    """
        Defines the Rectangle subclass of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialization attributes of the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
            Prints the rectangle instance to stdout using
            the '#' character
        """
        print("\n" * self.y +
              "\n".join(" " * self.x + "#" * self.width
                        for i in range(self.height)))

    def __str__(self):
        """
            Prints the rectangle attributes in the format
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        """
        msg = "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            Updates class attributes by assigning key/value argument to them
        """

        attributes = ["id", "width", "height", "x", "y"]
        for arg in range(len(args)):
            for attr in range(len(attributes)):
                if attr != arg:
                    setattr(self, attributes[attr], args[arg])
                    break

        if not args or len(args) == 0:
            for key, value in kwargs.items():
                for attr in range(len(attributes)):
                    if key == attributes[attr]:
                        setattr(self, attributes[attr], value)
                        break

    def to_dictionary(self):
        """
            Returns dictionary representation of a Rectangle
        """
        d_rep = {}
        d_rep["id"] = self.id
        d_rep["width"] = self.width
        d_rep["height"] = self.height
        d_rep["x"] = self.x
        d_rep["y"] = self.y
        return d_rep
