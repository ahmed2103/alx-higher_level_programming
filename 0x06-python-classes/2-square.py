#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
