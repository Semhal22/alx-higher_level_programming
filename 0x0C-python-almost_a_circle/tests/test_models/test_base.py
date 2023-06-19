import unittest
import sys
path_ = '/root/alx-higher_level_programming/0x0C-python-almost_a_circle'
sys.path.insert(0, path_)
from models.base import Base
from models import base


class TestBase(unittest.TestCase):
    def test_documentation(self):
      self.assertGreater(len(base.__doc__), 1)
      self.assertGreater(len(Base.__doc__), 1)
      self.assertGreater(len(Base.__init__.__doc__), 1)
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(4)
        self.b3 = Base(0)
        self.b4 = Base(-2)
    def test_values(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 4)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 5)
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
