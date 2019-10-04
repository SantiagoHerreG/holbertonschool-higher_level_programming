#!/usr/bin/python3
""" Module containing a function that prints some strings..
2- task in python Test-driven development project


"""


def say_my_name(first_name, last_name=""):
    """ Function that prints a name
    Args:
        first_name (str): name
        last_name (str): surname
    """

    if (first_name == "" or isinstance(first_name, str) is False):
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    if ord(first_name[0]) not in range(65, 91):
        raise TypeError("first_name must be a string")

    for letter in first_name[1:]:
        if ord(letter) not in range(97, 123):
            raise TypeError("first_name must be a string")

    if last_name != "":
        if ord(last_name[0]) not in range(65, 91):
            raise TypeError("last_name must be a string")

        for letter in last_name[1:]:
            if ord(letter) not in range(97, 123):
                raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
