#!/usr/bin/python3
"""Module containing Square class"""
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

        super().__init__(id = id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width of the rectangle getter"""
            return self._width
        @width.setter
        def height(self, value):
            """height of the rectangle setter"""
            if not isinstance(width, int):
                raise TypeError('width must be an integer')
            if not width > 0:
                raise ValueError('width must be a positive integer')
            self._width = value

        @property
        def height(self):
            """height of the rectangle getter"""
            return self._height
        @width.setter

        def height(self, value):
            """height of the rectangle setter"""
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if not height > 0:
                raise ValueError('height must be a positive integer')
            self._height = value
        @property
        def x(self):
            """x position of the rectangle"""
            return self._x

        @x.setter
        def x(self, value):
            """
            x position of the rectangle
            """
            if not isinstance(value, int):
                raise TypeError('x position must be an integer')
            if not value >= 0:
                raise ValueError('x must be positive')
            self._x = value
        @property
        def y(self):
            """getter for y position of the rectangle
            :return: y position of the"""
            return self._y
        @y.setter
        def y(self, value):
            """setter for y position of the rectangle"""
            if not isinstance(value, int):
                raise TypeError('y position must be an integer')
            if not value > 0:
                raise ValueError('y must be positive')
            self._y = value


