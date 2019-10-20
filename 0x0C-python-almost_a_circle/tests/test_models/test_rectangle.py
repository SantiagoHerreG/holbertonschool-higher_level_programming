#!/usr/bin/python3
"""Unittest for rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_1_case(self):
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

    def test_2_inherits(self):
        """ Checks if the Rectangle inherints from Base
        """
        r1 = Rectangle(1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_3_two_equals(self):
        """ Checks if the return is correct in case of repeated recs

        """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(5, 5)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 11)

    def test_4_variable_args(self):
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

    def test_5_args(self):
        """ Checks if the error is raised in case of different arguments

        """
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(10)
