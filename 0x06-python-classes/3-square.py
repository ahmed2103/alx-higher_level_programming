#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """Property to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an integer")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size