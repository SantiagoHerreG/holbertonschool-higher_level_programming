#!/usr/bin/python3
""" Module containing a function that divides all elem of a matrix..
1- task in python Test-driven development project


"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix..
    Args:
        matrix (list of list): matrix source
        div (int): divisor for the matrix
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) o\
f integers/floats")

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError("matrix must be a matrix (list of lists) o\
f integers/floats")
        for nums in rows:
            if (type(nums) is not int and type(nums) is not float):
                raise TypeError("matrix must be a matrix (list of lists) o\
f integers/floats")
                print(nums)
    length = len(matrix[0])
    for rows in matrix:
        if len(rows) != length:
            raise TypeError("Each row of the matrix must have the same size")

    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(x / div, 2) for x in row] for row in matrix]
