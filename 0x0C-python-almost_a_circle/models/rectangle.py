#!/usr/bin/python3
"""Class Rectangle that inherits from Base

"""
from models.base import Base


class Rectangle(Base):
    """New rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for new class, optional x, y args and id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the representation of the rectangle
        """
        for rows in range(self.__height):
            for col in range(self.__width):
                print("#", end="")
            print()
