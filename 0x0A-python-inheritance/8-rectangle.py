#!/usr/bin/python3
""" Class Rectangle

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
