#!/usr/bin/python3
"""Module containing Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class that represents a rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class
        :param width: width of the rectangle
        :param height: height of the rectangle
        :param x: x position of the rectangle
        :param y: y position of the rectangle
        :param id: id of the rectangle or its count if None
        :raise
        TypeError:if width, height or x or y are not integers
        ValueError: if width, height or x or y are not positive integers"""

        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle getter"""
        return self._width

    @width.setter
    def width(self, value):
        """width of the rectangle setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if not value > 0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def height(self):
        """height of the rectangle getter"""
        return self._height

    @height.setter
    def height(self, value):
        """height of the rectangle setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if not value > 0:
            raise ValueError('height must be > 0')
        self._height = value

    @property
    def x(self):
        """x position of the rectangle"""
        return self._x

    @x.setter
    def x(self, value):
        """x position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('x position must be an integer')
        if not value >= 0:
            raise ValueError('x must be >= 0')
        self._x = value

    @property
    def y(self):
        """y position of the rectangle"""
        return self._y

    @y.setter
    def y(self, value):
        """y position of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('y position must be an integer')
        if not value >= 0:
            raise ValueError('y must be >= 0')
        self._y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self._width * self._height

    def display(self):
        """method to represent the rectangle in stdout `#` units"""
        print('\n'.join('#' * self.width for _ in range(self.height)))

    def __str__(self):
        """method to represent the rectangle informally"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id, self.x, self.y, self.width, self.height)
