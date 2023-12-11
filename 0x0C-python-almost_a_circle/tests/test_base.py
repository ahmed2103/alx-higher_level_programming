#!/usr/bin/python3

import unittest
from io import StringIO
from models.base import Base 
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def setUp(self):
        self.base = Base()
        self.rect1 = Rectangle(3, 4, 5, 6, 1)
        self.rect2 = Rectangle(7, 8, 9, 10, 2)        
        self.capturer = StringIO()
        sys.stdout = self.capturer

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        """Ensure docstrings exist"""
        self.assertIsNotNone(Base.__doc__)        
        for method in dir(Base):
            if method.startswith("_"):
                continue
            self.assertIsNotNone(getattr(Base, method).__doc__)

    def test_id(self):
        """Test for auto-incrementing id"""
        id_values = []
        for _ in range(5):
            b = Base()
            id_values.append(b.id)        
        self.assertEqual(id_values, [1, 2, 3, 4, 5])        

    def test_to_from_json_string(self):
        """Test json conversion functions"""
        json_str = Base.to_json_string([self.rect1.to_dictionary()])
        list_output = Base.from_json_string(json_str)
        
        self.assertEqual(len(list_output), 1)        
        self.assertDictContainsSubset(self.rect1.to_dictionary(), 
                                      list_output[0])

        json_str = Base.to_json_string([r.to_dictionary() for r in [self.rect1, self.rect2]])
        list_output = Base.from_json_string(json_str)

        self.assertEqual(len(list_output), 2)
        self.assertDictContainsSubset(self.rect1.to_dictionary(), 
                                      list_output[0])
        self.assertDictContainsSubset(self.rect2.to_dictionary(),
                                      list_output[1])

if __name__ == "__main__":
    unittest.main()
