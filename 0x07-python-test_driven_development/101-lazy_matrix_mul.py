#!/usr/bin/python3
""" Module containing a function that multiplies 2 matrices

6- task in python Test-driven development project


"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that returns the multiplication of two matrices
    Args:

        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for rows_a in m_a:
        if type(rows_a) is not list:
            raise TypeError("m_a must be a list of lists")

    for rows_b in m_b:
        if type(rows_b) is not list:
            raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    for rows_a in m_a:
        for nums in rows_a:
            if (type(nums) is not int and type(nums) is not float):
                raise TypeError("m_a should contain only integers or floats")
    for rows_b in m_b:
        for nums in rows_b:
            if (type(nums) is not int and type(nums) is not float):
                raise TypeError("m_b should contain only integers or floats")

    length_a = len(m_a[0])
    for rows in m_a:
        if len(rows) != length_a:
            raise TypeError("each row of m_a must be of the same size")
    length_b = len(m_b[0])
    for rows in m_b:
        if len(rows) != length_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    a = np.array(m_a)
    b = np.array(m_b)

    return a.dot(b)
