#!/usr/bin/python3
"""Unittest for square.py
"""
import unittest
from models.base import Base
from models.square import Square
import io
import sys


def setUpModule():
    """Resets the Base Class for the module
    """
    Base._Base__nb_objects = 0


class TestSquare(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_01_Square(self):
        """Tests the new subclass Square
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        with self.assertRaises(TypeError) as cm:
            s1 = Square()

        s2 = Square(3, 3)
        self.assertEqual(s2.area(), 9)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)

        s3 = Square(7, 2, 7)
        self.assertEqual(s3.area(), 49)
        self.assertEqual(s3.width, 7)
        self.assertEqual(s3.height, 7)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 7)
        self.assertEqual(s3.id, 3)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.area(), 1)
        self.assertEqual(s4.width, 1)
        self.assertEqual(s4.height, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 4)
        with self.assertRaises(TypeError) as cm:
            s1 = Square(1, 2, 3, 4, 5)

    def test_02_Square_exceptions(self):
        """Checks exceptions in Square class
        """
        with self.assertRaises(TypeError) as cm:
            Square("hi", 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, "hi", 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, "hi", 10)
        self.assertTrue("y must be an integer" in str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            Square([], 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square({}, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square((), 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(1.5, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(True, 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, [], 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, {}, 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, (), 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 1.5, 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, True, 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, [], 10)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, {}, 10)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, (), 10)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, 1.5, 10)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, True, 10)
        self.assertTrue("y must be an integer" in str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            Square(-5, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Square(0, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Square(10, -5, 10, 10)
        self.assertTrue("x must be >= 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Square(10, 10, -5, 10)
        self.assertTrue("y must be >= 0" in str(cm.exception))

    def test_03_Square_str(self):
        """Checks the string representation of a Square
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        s1 = Square(1)                   # Call function
        s1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '#\n')
        with self.assertRaises(TypeError):
            s1.display(10)

    def test_04_str_Square_bigger(self):
        """ Tests the str method for printing the rectangle
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        s1 = Square(2, 3, 1, 100)              # Call function
        print(s1)
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '[Square] (100) 3/1 - 2\n')

    def test_05_Square_str(self):
        """Checks the display() representation of a Square
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        s1 = Square(2, 2, 2)                   # Call function
        s1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '\n\n  ##\n  ##\n')

    def test_06_Square_str(self):
        """Checks the display() representation of a Square
        """
        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        s1 = Square(2, 2)                   # Call function
        s1.display()
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '  ##\n  ##\n')
