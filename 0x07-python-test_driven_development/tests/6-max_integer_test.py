"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 8, 2]), 8)
        self.assertEqual(max_integer([8, 3, 4]), 8)
        self.assertEqual(max_integer([4, -2, 5]), 5)
        self.assertEqual(max_integer([-3, -6, -8]), -3)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([]), None)
