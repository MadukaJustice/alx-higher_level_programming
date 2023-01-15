#!/usr/bin/python3
"""
    Square class Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Defines the Square subclass of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialization attributes of the Rectangle class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
            size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            Prints the square attributes in the format
            '[Square] (<id>) <x>/<y> - <width>/<height>'
        """
        msg = "[Square] ({}) {:d}/{:d} - {:d}"
        return msg.format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
            Updates class attributes by assigning key/value argument to them
        """

        attributes = ["id", "size", "x", "y"]
        for arg in range(len(args)):
            for attr in range(len(attributes)):
                if attr == arg:
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
            Returns dictionary representation of a Square
        """
        d_rep = {}
        d_rep["id"] = self.id
        d_rep["size"] = self.size
        d_rep["x"] = self.x
        d_rep["y"] = self.y
        return d_rep
