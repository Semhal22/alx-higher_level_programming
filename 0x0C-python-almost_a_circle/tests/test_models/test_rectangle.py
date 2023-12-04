#!/usr/bin/python3
"""Test for the module rectangle"""
import models
from models.rectangle import Rectangle
from models import rectangle
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Tests the Rectangle class"""
    def test_module_documentation(self):
        """Documentation for the module"""
        self.assertGreater(len(rectangle.__doc__), 1)

    def test_class_documentation(self):
        """Documentation of the class Rectangle"""
        self.assertGreater(len(Rectangle.__doc__), 1)

    def test_func_documentation(self):
        """Documentation of the function init"""
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_values(self):
        """Check if correct id's are set to instances of the Rectangle class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 3, 4, 14)
        self.assertEqual(r3.id, 14)

        r4 = Rectangle(2, 3)
        self.assertEqual(r4.id, 3)
