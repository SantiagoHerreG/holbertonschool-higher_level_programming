#!/usr/bin/python3
""" Module containing add function of two numbers.
Zero task in python Test-driven development project


"""


def add_integer(a, b=98):

    """ Function that adds 2 integers or floats.
    Args:
        a (int): first number
        b (int): second number, 98 by default
    """
    if (a is None or (type(a) is not int and type(a) is not float)):
        raise TypeError("a must be an integer")
    if (b is None or (type(b) is not float and type(b) is not int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
