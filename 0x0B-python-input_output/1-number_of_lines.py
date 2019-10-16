#!/usr/bin/python3
"""Function that returns the number of lines of a text file

"""


def number_of_lines(filename=""):
    """ Counts the number of lines in a file
    """
    with open(filename, encoding='UTF-8') as f:

        count = 0
        for lines in f:
            count += 1
    return count
