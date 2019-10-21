#!/usr/bin/python3
"""Unittest for rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys


def setUpModule():
    """Resets the Base Class for the module
    """
    Base._Base__nb_objects = 0


class TestRectangle(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """

    def test_001_case(self):
        """ Checks if the return is correct

        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_002_inherits(self):
        """ Checks if the Rectangle inherints from Base
        """
        r1 = Rectangle(1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_003_two_equals(self):
        """ Checks if the return is correct in case of repeated recs

        """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(5, 5)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r2.id, 5)

    def test_004_variable_args(self):
        """ Checks if the return is correct in case of variable args

        """
        r1 = Rectangle(10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 7)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 20)

    def test_005_args(self):
        """ Checks if the error is raised in case of different arguments

        """
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_006_validate_integer(self):
        """Tests all possible combination of datatypes
        """
        with self.assertRaises(TypeError) as cm:
            Rectangle("hi", 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "hi", 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, "hi", 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, "hi")
        self.assertTrue("y must be an integer" in str(cm.exception))

    def test_007_validate_integer_empty(self):
        """ Empty data types to evaluate
        """
        with self.assertRaises(TypeError) as cm:
            Rectangle([], 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle({}, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle((), 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(1.5, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(True, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, [], 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, {}, 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, (), 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 1.5, 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, True, 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, [], 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, {}, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, (), 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 1.5, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, True, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, [])
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, {})
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, ())
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, 1.5)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, True)
        self.assertTrue("y must be an integer" in str(cm.exception))

    def test_008_checks_value(self):
        """Checks negative and zero values
        """

        with self.assertRaises(ValueError) as cm:
            Rectangle(-5, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -5, 10, 10)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 0, 10, 10)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 10, -5, 10)
        self.assertTrue("x must be >= 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 10, 10, -5)
        self.assertTrue("y must be >= 0" in str(cm.exception))

    def test_009_area(self):
        """Checks correct return and error if argument passed to area.
        """
        r1 = Rectangle(10, 10, 0, 0, 10)
        self.assertEqual(r1.area(), 100)
        with self.assertRaises(TypeError):
            r1.area(10)

    def test_010_display_rectangle(self):
        """ Tests printing in stdout
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        r1 = Rectangle(4, 6)              # Call function
        r1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '####\n####\n####\n####\n\
####\n####\n')

    def test_011_display_small_rectangle(self):
        """ Tests printing in stdout
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        r1 = Rectangle(1, 1)              # Call function
        r1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '#\n')
        with self.assertRaises(TypeError):
            r1.display(10)

    def test_012_str_method(self):
        """ Tests the str method for printing the rectangle
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        r1 = Rectangle(1, 1)              # Call function
        print(r1)
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '[Rectangle] (40) 0/\
0 - 1/1\n')

    def test_013_display_rectangle_x_y(self):
        """ Tests printing in stdout
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        r1 = Rectangle(2, 3, 2, 3)              # Call function
        r1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '\n\n\n  ##\n  ##\n  ##\n')

    def test_014_update(self):
        """ Test the update method
        """
        r1 = Rectangle(10, 10)
        r1.update(7, 20, 20, 10, 10)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_015_update_args(self):
        """ Checks number of args in update method
        """
        r1 = Rectangle(7, 7, 0, 0, 1)
        r1.update()
        self.assertEqual(r1.id, 43)
        with self.assertRaises(TypeError):
            r1.update(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError) as cm:
            r1.update(10, [], 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(10, 10, [], 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(10, 10, 10, [], 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(10, 10, 10, 10, [])
        self.assertTrue("y must be an integer" in str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r1.update(10, -5, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(10, 0, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(10, 10, -5, 10, 10)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(10, 10, 0, 10, 10)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(10, 10, 10, -5, 10)
        self.assertTrue("x must be >= 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(10, 10, 10, 10, -5)
        self.assertTrue("y must be >= 0" in str(cm.exception))

    def test_016_kwargs(self):
        """Tests new updates of attributes using kwargs
        """
        r1 = Rectangle(7, 7, 0, 0, 100)
        r1.update(id=75)
        self.assertEqual(r1.id, 75)
        r1.update(width=1, height=1, id=1, x=1, y=1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        r1.update(height=2, x=2, id=2, width=2, y=2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)

        with self.assertRaises(TypeError) as cm:
            r1.update(width=[])
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(height=[])
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(x=[])
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1.update(y=[])
        self.assertTrue("y must be an integer" in str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r1.update(width=-5)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(width=0)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(height=-5)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(height=0)
        self.assertTrue("height must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(x=-5)
        self.assertTrue("x must be >= 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1.update(y=-5)
        self.assertTrue("y must be >= 0" in str(cm.exception))

    def test_017_kwargs(self):
        """Tests kwargs not matching or avoided
        """
        r1 = Rectangle(7, 7, 0, 0, 100)
        r1.update(id=-5)
        self.assertEqual(r1.id, -5)
        r1.update(wid=1, heig=1, id=1, x=1, y=1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        r1.update(nn=0)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        r1.update(100, width=100, x=100)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.x, 1)
