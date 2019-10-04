#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_case(self):
        """ Checks if the return is correct

        """
        res = max_integer([1, 2, 3])
        self.assertEqual(res, 3)

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
