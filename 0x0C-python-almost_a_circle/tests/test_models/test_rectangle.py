#!/usr/bin/python3
"""Unittest for rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_001_case(self):
        """ Checks if the return is correct

        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r2.id, 8)
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
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 11)

    def test_004_variable_args(self):
        """ Checks if the return is correct in case of variable args

        """
        r1 = Rectangle(10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 13)
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
