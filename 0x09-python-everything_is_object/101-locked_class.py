#!/usr/bin/python3
""" Class with immutable behaviour """


class LockedClass:
    """ Only allowed the attribute first_name

    """
    __slots__ = "first_name",
