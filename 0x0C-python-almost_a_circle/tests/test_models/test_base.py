#!/usr/bin/python3

import models
from models.base import Base
from models import base
import unittest


class TestBase(unittest.TestCase):
    """Tests the base class"""
    def test_module_documentation(self):
        """Documentation for the module"""
        self.assertGreater(len(base.__doc__), 1)

    def test_class_documentation(self):
        """Documentation of the class Base"""
        self.assertGreater(len(Base.__doc__), 1)

    def test_func_documentation(self):
        """Documentation of the function init"""
        self.assertGreater(len(Base.__init__.__doc__), 1)

    def test_values(self):
        """Check if correct id's are set to instances of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)
