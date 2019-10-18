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
        self.__width = value

    @property
    def height(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ Setter and getters for the Rectangle instance attributes
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
