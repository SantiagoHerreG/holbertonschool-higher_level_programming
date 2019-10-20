#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_case(self):
        """ Checks if the return is correct

        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_zero(self):
        """ Checks if the return is correct in case of id = 0
        """
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_negatives(self):
        """ Checks if the return is correct in case of negative id

        """
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_two_equals(self):
        """ Checks if the return is correct in case of repeated ids

        """
        b1 = Base(1)
        b2 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 6)

    def test_more_args(self):
        """ Checks if the error is raised in case of more arguments

        """
        self.assertRaises(TypeError, Base(), 1, 2)
