#!/usr/bin/python3
""" Subclass Rectangle
Subclass Square
Class BaseGoemetry
"""


class BaseGeometry:
    """ New class"""
    def integer_validator(self, name, value):
        """ Checks and validates the values"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")

    def area(self):
        """ Raises an error
        """
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """ New class Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ New area attribute"""
        self.area = self.__width * self.__height

        return self.area

    def __str__(self):
        """ String representation of the rectangle
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """ New Subclass"""
    def __init__(self, size):
        """ Creates a square by using the super() method"""
        super().__init__(size, size)
        self.__size = size
