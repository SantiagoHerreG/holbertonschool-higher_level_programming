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
