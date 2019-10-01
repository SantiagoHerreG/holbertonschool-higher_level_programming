#!/usr/bin/python3
class Square:
    """Class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method for the class.

        An error is raise in case the arg is not an int or less than 0,
        or the position is not a tuple of natural numbers or zero.

        Args:
            size (int): size of the square side.
            position (tuple): tuple for position
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(position[0]) is not int) or position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(position[1]) is not int) or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """int: The value for __size method is handled by size getter and setter..

        The setter checks if the new value is an int and raise the error.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """int: The value for __position method is handled by size getter and setter.

        The setter checks if the new value is a tuple with integers and
        and raise coresponding error.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[0]) is not int) or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[1]) is not int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Class method for area calculation.

        Returns:
            The area of th square..
        """
        return self.__size ** 2

    def my_print(self):
        """Class method for printing the square in #'s.
        The position is used to print header spaces/underscores in each line.

        Returns:
            Void
        """
        if self.__size:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    if (self.__position[1] == 0):
                        print(" ", end="")
                    else:
                        print("_", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
