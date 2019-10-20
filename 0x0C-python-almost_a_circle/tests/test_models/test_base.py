#!/usr/bin/python3
"""Unittest for max_integer([..])
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

'''
   def test_empty(self):
        """ Checks if the return is None in case of empty list

        """
        res = max_integer([])
        self.assertIsNone(res)

    def test_unique(self):
        """ Checks if the return is correct in case of one element

        """
        res = max_integer([1])
        self.assertEqual(res, 1)

    def test_two_equals(self):
        """ Checks if the return is correct in case of repeated elements

        """
        res = max_integer([0, 1, 2, 3, 3, 2])
        self.assertEqual(res, 3)

    def test_negatives(self):
        """ Checks if the return is correct in case of negative elements

        """
        res = max_integer([-4, -2, -1])
        self.assertEqual(res, -1)

    def test_first_is_max(self):
        """ Checks if the return is correct in case of first element is max

        """
        res = max_integer([10, 8, 7, 1])
        self.assertEqual(res, 10)
'''
