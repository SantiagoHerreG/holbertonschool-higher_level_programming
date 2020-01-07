#!/usr/bin/python3
""" Contains a function that uses binary search
"""


def recursion_peak(int_list, idx1, idx2):
    """ Recursion for finding a peak
    """
    idx = int((idx2 - idx1)/2) + idx1
    current = int_list[idx]
    if idx == idx1 or idx == idx2:
        return current

    if (current > int_list[idx + 1] and current > int_list[idx - 1]):
        return current
    elif current < int_list[idx - 1]:
        return recursion_peak(int_list, idx1, idx - 1)
    else:
        return recursion_peak(int_list, idx + 1, idx2)


def find_peak(list_of_integers):
    """Function that returns a peak in a list of integers
    """
    length = len(list_of_integers)

    if (length == 0):
        return None
    return recursion_peak(list_of_integers, 0, length - 1)
