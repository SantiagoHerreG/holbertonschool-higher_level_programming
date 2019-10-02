#!/usr/bin/python3
import math


class Circle:
    def __init__(self, radius=0):
        """Dissasembled from python bytecode.
        Args:
            radius (str): constant number. """
        self._MagicClass__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area of a circle."""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference length of a circle."""
        return 2 * math.pi * self._MagicClass__radius
