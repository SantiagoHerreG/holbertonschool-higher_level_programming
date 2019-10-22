#!/usr/bin/python3
"""Class Square that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New square class that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square instances
        """
        self.size = size
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def size(self):
        """ Getter and setter methods for the instance attribute __size
        Validation of the input is done by the Rectangle superclass update.
        """
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """Overrides the string method
        """
        return "[Square] " + "(" + str(self.id) + ") " + str(self.x) + "\
/" + str(self.y) + " - " + str(self.width)

    def update(self, *args, **kwargs):
        """Updates a Square, kwargs not taken into account if *args
        """
        length = len(args)
        len_kw = len(kwargs)
        if length == 0 and len_kw == 0:
            super(Rectangle, self).__init__(None)
            return
        if length > 4:
            raise TypeError("update takes a maximum of 4 *args")

        if length:

            super(Rectangle, self).__init__(args[0])

            if length >= 2:
                self.width = args[1]
                self.height = args[1]
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length == 4:
                self.y = args[3]

        elif len_kw:

            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    super(Rectangle, self).__init__(value)

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Square
        """
        to_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return to_dict
