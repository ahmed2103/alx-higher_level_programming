#!/usr/bin/python3
"""Module implementing a Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a Square as a subclass of Rectangle"""
    def __init__(self, size):
        """Initialize a new Square instance
        
        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute the area of the Square"""
        return self.__size ** 2
