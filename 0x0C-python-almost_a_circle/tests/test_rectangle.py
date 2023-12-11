#!/usr/bin/python3

import unittest
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.rect1 = Rectangle(3, 4, 5, 6, 1)        
        self.rect2 = Rectangle(7, 8, 9, 10, 2)
        self.capturer = StringIO()        
        sys.stdout = self.capturer

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_pep8(self):
        """Pep8 compliance"""
        self.asses_pep8_compliance(["models/rectangle.py"])

    def test_inheritance(self):
        """Test inheritance from Base"""
        self.assertIsInstance(self.rect1, Base)

    def test_init(self):
        """Test initialization"""
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect1.width, 3)
        # ...        

    def test_str(self):
        """Test __str__ magic method"""
        self.assertEqual(str(self.rect1), "[Rectangle] (1) 5/6 - 3/4")

    def test_display(self):
        """Test display method prints rectangle"""
        self.rect1.display()
        display = self.capturer.getvalue()
        self.assertIn("####\n####\n####", display)

    def test_to_dict(self):
        """Test conversion to dictionary"""
        d = self.rect1.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 3, 'height': 4, 'x': 5, 'y': 6})
        
    def test_create(self):
        """Test create method"""
        r = Rectangle.create(**self.rect1.to_dictionary())
        self.assertIsNot(r, self.rect1)
        self.assertDictEqual(r.to_dictionary(), self.rect1.to_dictionary())

if __name__ == '__main__':
    unittest.main()
