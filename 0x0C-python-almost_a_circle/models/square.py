#!/usr/bin/python3
"""Class Square that inherits from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New square class that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square instances
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the string method
        """
        return "[Square] " + "(" + str(self.id) + ") " + str(self.x) + "\
/" + str(self.y) + " - " + str(self.width)
