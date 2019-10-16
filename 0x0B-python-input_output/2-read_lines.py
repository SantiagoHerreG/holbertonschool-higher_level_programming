#!/usr/bin/python3
"""Function that reads n lines of a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    """ Reads a certain number of lines in a file
    """
    with open(filename, encoding='UTF-8') as f:

        if nb_lines <= 0:
            print(f.read(), end="")
            return
        count = 0
        for lines in f:
            count += 1
            if count <= nb_lines:
                print(lines, end="")
            else:
                return
