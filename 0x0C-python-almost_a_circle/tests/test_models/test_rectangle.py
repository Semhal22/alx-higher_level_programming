#!/usr/bin/python3
"""Test for the module rectangle"""
import models
from models.rectangle import Rectangle
from models import rectangle
from models.base import Base
import json
import unittest
from unittest.mock import patch, call


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

    def setUp(self):
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

    def test_types(self):
        """Check the validation of all the parameters"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(TypeError):
            Rectangle("10", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(2, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(2, 1, 4, -4)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test the method area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    @patch('builtins.print')
    def test_display(self, mock_print):
        """Test the display method that prints the rectangle using #"""
        r1 = Rectangle(1, 2)
        r1.display()

        mock_print.assert_has_calls([call("#", end=""), call(),
                                    call("#", end="")])

        # r2 = Rectangle(1, 2, 0, 2)
        # mock_print.assert_has_calls([call(), call(), call("#", end=""),
        # call(), call("#", end="")])

    def test_str(self):
        """Tests how the class is printed"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_str = str(r1)

        self.assertEqual(r1_str, "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Tests if the object is really updated"""
        r1 = Rectangle(10, 10, 10, 10)
        r1_str = str(r1)

        self.assertEqual(r1_str, "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

        r1.update(height=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/2")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/5 - 1/2")

        r1.update(x=1, height=2, y=3, width=4, id=23)
        self.assertEqual(str(r1), "[Rectangle] (23) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Tests the method to_dictionary of the Rectangle class"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")

        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                   'width': 10})
        self.assertIsInstance(r1_dict, dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")

        r2.update(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

    def test_to_json(self):
        """Tests the method to_json_string of the Base class static method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])

        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1,
                                      'height': 7, 'y': 8})
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary, json.loads(json_dictionary)[0])
        self.assertIsInstance(json_dictionary, str)

    def test_save_to_file(self):
        """Tests class method of Base save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            list_objs = json.load(f)
        self.assertEqual(r1.to_dictionary(), list_objs[0])
        self.assertEqual(r2.to_dictionary(), list_objs[1])

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
