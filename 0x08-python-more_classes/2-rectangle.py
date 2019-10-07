#!/usr/bin/python3
""" Module for the class Rectangle
0 task of Python - More Classes and Objects

"""


class Rectangle:
    """ Class that defines a rectangle

    """
    def __init__(self, width=0, height=0):
        """ __init__ method for the class.

        An error is raise in case the arg is not an int or less than 0,
.

        Args:
            width (int): size.
            heigth (tuple): size
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """The value for __heigth method is handled by size getter and setter..

        The setter checks if the new value is an int and raise the error.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """The value for __width method is handled by width getter and setter.

        The setter checks if the new value is an int or negative and
        raise the error.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Class method for area calculation.

        Returns:
            The area of the rectangle..
        """
        return self.__width * self.__height

    def perimeter(self):
        """Class method for perimeter calculation.
        Checks if any size is zero before calculation

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height
