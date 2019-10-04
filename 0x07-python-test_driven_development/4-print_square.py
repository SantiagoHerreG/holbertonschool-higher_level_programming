#!/usr/bin/python3
""" Module containing a function that prints a
square with the character #.
4- task in python Test-driven development project


"""


def print_square(size):
    """ Function that prints a square of #'s
    Args:

        size (int): size of the square
    """

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
