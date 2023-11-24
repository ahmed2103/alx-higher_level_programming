#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_one(self):
        """Test case: list of integers in ascending order"""
        matrix1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(matrix1), 4)

    # ... (similar comments for each test case)

    def test_ten(self):
        """Test case: list of integers in random order"""
        matrix1 = [1, 2, 6, 5, 4]
        self.assertEqual(max_integer(matrix1), 6)

if __name__ == '__main__':
    unittest.main()
