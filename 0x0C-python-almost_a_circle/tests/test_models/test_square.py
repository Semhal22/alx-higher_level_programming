#!/usr/bin/python3
"""Test for the module square"""
import models
from models.rectangle import Rectangle
from models.square import Square
from models import square
from models.base import Base
import unittest
from unittest.mock import patch, call


class TestBase(unittest.TestCase):
    """Tests the Square class"""
    def test_module_documentation(self):
        """Documentation for the module"""
        self.assertGreater(len(square.__doc__), 1)

    def test_class_documentation(self):
        """Documentation of the class Square"""
        self.assertGreater(len(square.__doc__), 1)

    def test_func_documentation(self):
        """Documentation of the function init"""
        self.assertGreater(len(Square.__init__.__doc__), 1)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_values(self):
        """Check if correct id's are set to instances of the Square class"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 10)
        self.assertEqual(s2.id, 2)

        s3 = Square(2, 3, 4, 14)
        self.assertEqual(s3.id, 14)

    def test_types(self):
        """Check the validation of all the parameters"""
        with self.assertRaises(TypeError):
            s = Square(10, 2)
            s.size = "9"

        with self.assertRaises(TypeError):
            Square(10, "2")

        with self.assertRaises(TypeError):
            Square("2")

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            s = Square(10, 2)
            s.width = -10

        with self.assertRaises(TypeError):
            s = Square(10, 2)
            s.x = {}

        with self.assertRaises(ValueError):
            Square(2, 3, -1)

    def test_area(self):
        """Test the method area"""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

        s2 = Square(3, 1, 3)
        self.assertEqual(s2.area(), 9)

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Test the display method that prints the squaree using #"""
        s1 = Rectangle(1, 2)
        s1.display()

        mock_print.assert_has_calls([call("#", end=""), call(),
                                    call("#", end="")])

        # r2 = Rectangle(1, 2, 0, 2)
        # mock_print.assert_has_calls([call(), call(), call("#", end=""),
        # call(), call("#", end="")])

    def test_str(self):
        """Tests how the class is printed"""
        s1 = Square(2, 2)
        s1_str = str(s1)

        self.assertEqual(s1_str, "[Square] (1) 2/0 - 2")

        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 10")

    def test_update(self):
        """Tests if the object is really updated"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(x=1, size=7, y=3, id=23)
        self.assertEqual(str(s1), "[Square] (23) 1/3 - 7")

    def test_to_dictionary(self):
        """Tests the method to_dictionary of the Square class"""
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")

        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertIsInstance(s1_dict, dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")

        s2.update(**s1_dict)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)
