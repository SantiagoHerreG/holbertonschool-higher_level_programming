#!/usr/bin/python3
""" Module for the class Rectangle
Python - More Classes and Objects

"""


class Rectangle:
    """ Class that defines a rectangle

    """

    number_of_instances = 0
    """ int: number of instances initiallized """
    print_symbol = "#"
    """ (any type): symbol used for printing the rectangule __str__ method"""

    def __init__(self, width=0, height=0):
        """ __init__ method for the class.

        An error is raise in case the arg is not an int or less than 0,
.
        Args:
            width (int): size.
            heigth (tuple): size
        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

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

    def __repr__(self):
        """ Magic method that returns the representation of the instance
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.height) + ")"

    def __str__(self):
        """ Magic method that allows print() and str() to print the rectangule
        in #'s

        """
        string = ""
        for rows in range(self.__height):
            for columns in range(self.__width):
                string += str(self.print_symbol)
                if columns + 1 == self.__width and rows + 1 < self.__height:
                    string += '\n'
        return string

    def __del__(self):
        """ Destructor for the instances of Rectangle class.
        Prints a good bye message.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the Area

        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a new instance of the Rectangle class
        with same size of width and height
        """
        return cls(size, size)
