#!/usr/bin/python3
class Square:
    """Class that defines a square.
    """
    def __init__(self, size=0):
        """ __init__ method for the class.

        An error is raise in case the arg is not an int or less than 0.

        Args:
            size (int): size of the square side.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

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

    def area(self):
        """Class method for area calculation.

        Returns:
            The area of th square..
        """
        return self.__size ** 2

    def my_print(self):
        """Class method for printing the square in #'s.

        Returns:
            Void
        """
        if self.__size:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
