#!/usr/bin/python3
""" Contains a function that uses binary search
"""


def recursion_peak(int_list, idx):
    """ Recursion for finding a peak
    """
    current = int_list[idx]
    if idx == 0 or idx == len(int_list) - 1:
        return current

    if idx + 1 < len(int_list):
        if (current > int_list[idx + 1] and current > int_list[idx - 1]):
            return current
        elif current < int_list[idx - 1]:
            return recursion_peak(int_list, idx - 1)
        elif current < int_list[idx + 1]:
            return recursion_peak(int_list, idx + 1)
        else:
            return max(recursion_peak(int_list, idx + 1),
                       recursion_peak(int_list, idx - 1))
    else:
        return current


def find_peak(list_of_integers):
    """Function that returns a peak in a list of integers
    """
    length = len(list_of_integers)
    idx = int(length/2)

    if (length == 0):
        return None
    return recursion_peak(list_of_integers, idx)
