#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys
import os


def setUpModule():
    """Resets the Base Class for the module
    """
    Base._Base__nb_objects = 0


def tearDownModule():
    """Resets the Base Class for the module
    """
    Base._Base__nb_objects = 0


class TestBase(unittest.TestCase):
    """Test cases using Unittest, this class is a subclass of unittest.TestCase

    """
    def test_01_case(self):
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

    def test_02_zero(self):
        """ Checks if the return is correct in case of id = 0
        """
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_03_negatives(self):
        """ Checks if the return is correct in case of negative id

        """
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_04_two_equals(self):
        """ Checks if the return is correct in case of repeated ids

        """
        b1 = Base(1)
        b2 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 5)

    def test_05_more_args(self):
        """ Checks if the error is raised in case of more arguments

        """
        self.assertRaises(TypeError, Base(), 1, 2)

    def test_06_json_serialization(self):
        """Tests the returns the JSON string rep of list_dictionaries
        """
        with self.assertRaises(TypeError):
            Base.to_json_string("hi")
        with self.assertRaises(TypeError):
            Base.to_json_string(())
        with self.assertRaises(TypeError):
            Base.to_json_string({})
        with self.assertRaises(TypeError):
            Base.to_json_string(True)
        with self.assertRaises(TypeError):
            Base.to_json_string(2.5)
        with self.assertRaises(TypeError):
            Base.to_json_string(["hi"])
        with self.assertRaises(TypeError):
            Base.to_json_string([[]])
        with self.assertRaises(TypeError):
            Base.to_json_string([()])
        with self.assertRaises(TypeError):
            Base.to_json_string([2.5])
        with self.assertRaises(TypeError):
            Base.to_json_string([True])
        with self.assertRaises(TypeError):
            Base.to_json_string()

        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, "[]")

        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

        r1 = Rectangle(1, 2, 3, 4, 100)
        new_json = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(new_json), str)

        capturedOutput = io.StringIO()   # Create StringIO object
        sys.stdout = capturedOutput      # and redirect stdout
        print(Base.to_json_string([{"hello": "world"}]))
        sys.stdout = sys.__stdout__      # Reset redirect
        self.assertEqual(capturedOutput.getvalue(), '[{"hello": "world"}]\n')

    def test_07_file_json(self):
        """Checks the JSON string representation in a file
        """
        with self.assertRaises(TypeError):
            Base.save_to_file("hi")
        with self.assertRaises(TypeError):
            Base.save_to_file(())
        with self.assertRaises(TypeError):
            Base.save_to_file({})
        with self.assertRaises(TypeError):
            Base.save_to_file(True)
        with self.assertRaises(TypeError):
            Base.save_to_file(2.5)
        with self.assertRaises(TypeError):
            Base.save_to_file(["hi"])
        with self.assertRaises(TypeError):
            Base.save_to_file([[]])
        with self.assertRaises(TypeError):
            Base.save_to_file([()])
        with self.assertRaises(TypeError):
            Base.save_to_file([2.5])
        with self.assertRaises(TypeError):
            Base.save_to_file([True])
        with self.assertRaises(TypeError):
            Base.save_to_file()

        Base.save_to_file(None)
        self.assertTrue(os.path.isfile('Base.json'))
        with open("Base.json", encoding="UTF-8") as f:
            self.assertEqual(f.read(), "[]")

        Base.save_to_file([])
        self.assertTrue(os.path.isfile('Base.json'))
        with open("Base.json", encoding="UTF-8") as f:
            self.assertEqual(f.read(), "[]")

        r1 = Rectangle(2, 2)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.isfile('Rectangle.json'))

        s1 = Square(5, 1, 1, 1)
        Square.save_to_file([s1])
        self.assertTrue(os.path.isfile('Square.json'))

    def test_08_from_json_str(self):
        """Checks the JSON string representation in a file
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([])
        with self.assertRaises(TypeError):
            Base.from_json_string(())
        with self.assertRaises(TypeError):
            Base.from_json_string({})
        with self.assertRaises(TypeError):
            Base.from_json_string(True)
        with self.assertRaises(TypeError):
            Base.from_json_string(2.5)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string([])
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(())
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({})
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(True)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(2.5)
        with self.assertRaises(TypeError):
            Square.from_json_string([])
        with self.assertRaises(TypeError):
            Square.from_json_string(())
        with self.assertRaises(TypeError):
            Square.from_json_string({})
        with self.assertRaises(TypeError):
            Square.from_json_string(True)
        with self.assertRaises(TypeError):
            Square.from_json_string(2.5)

        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])
        json_list = Base.from_json_string("")
        self.assertEqual(json_list, [])
        json_list = Base.from_json_string('["hi"]')
        self.assertEqual(json_list, ["hi"])
        json_list = Rectangle.from_json_string('[{"hi": "world"}]')
        self.assertEqual(json_list, [{'hi': 'world'}])
        json_list = Square.from_json_string('[]')
        self.assertEqual(json_list, [])
