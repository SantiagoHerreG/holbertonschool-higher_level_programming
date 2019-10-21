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
        for lines in range(self.__y):
            print()
        for rows in range(self.__height):
            for spaces in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the string method
        """
        return "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x) + "\
/" + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """Method that updates a rectangle
        """
        length = len(args)
        len_kw = len(kwargs)
        if length == 0 and len_kw == 0:
            super().__init__(None)
            return
        if length > 5:
            raise TypeError("update takes a maximum of 5 *args")

        if length:

            super().__init__(args[0])

            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length == 5:
                self.y = args[4]
        elif len_kw:

            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    super().__init__(value)
