import unittest
from models.square import Square  
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.sq1 = Square(4, 5, 6, 1)
        self.sq2 = Square(8, 9, 10, 2)  
        self.capturer = StringIO()
        sys.stdout = self.capturer      

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_inheritance(self):
        """Test inheritance relationships"""
        self.assertIsInstance(self.sq1, Rectangle)
        self.assertIsInstance(self.sq1, Base)

    def test_init(self):
        """Test initialization"""        
        self.assertEqual(self.sq1.width, 4)
        self.assertEqual(self.sq1.height, 4)
        self.assertEqual(self.sq1.x, 5)
        self.assertEqual(self.sq1.y, 6)

    def test_area(self):
        """Test area calculation"""
        self.assertEqual(self.sq1.area(), 16)

    def test_display(self):
        """Test display outputs square"""
        self.sq1.display()
        output = self.capturer.getvalue()
        self.assertIn("####\n####\n####\n####\n", output) 

    def test_update(self):
        """Test update method"""
        self.sq1.update(89, 2, 3, 4)
        self.assertEqual(str(self.sq1), "[Square] (89) 3/4 - 2")
        
    def test_to_dict(self):
        """Test conversion to dict"""
        d = self.sq1.to_dictionary()
        self.assertEqual(d, {'id': 1, 'size': 4, 'x': 5, 'y': 6})

    def test_create(self):
        """Test create method"""
        s = Square.create(**self.sq1.to_dictionary())
        self.assertIsNot(self.sq1, s)
        self.assertDictEqual(self.sq1.to_dictionary(), s.to_dictionary())
        
if __name__ == '__main__':
    unittest.main()
