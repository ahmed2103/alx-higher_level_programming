#!/usr/bin/python3
"""Module implementing the BaseGeometry class"""


class BaseGeometry:
    """A class serving as the base for geometry-related operations"""
    def area(self):
        """Computes the area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates whether the given value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
