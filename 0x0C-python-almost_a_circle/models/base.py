#!/usr/bin/python3
"""This class will be the base of all other classes in this project.
"""


class Base:
    """Base class with object id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of the class, id is optional
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
