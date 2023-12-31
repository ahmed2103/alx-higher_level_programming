#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """This class represents a rectangle object"""

    def __init__(self, width=0, height=0):
        """Creates a rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width"""
        return self._width

    @property
    def height(self):
        """Gets height"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value
