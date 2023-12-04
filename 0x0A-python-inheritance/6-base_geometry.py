#!/usr/bin/python3
"""Module implementing the BaseGeometry class"""


class BaseGeometry:
    """Defines the BaseGeometry class"""
    def __init__(self):
        """Initializes a new instance of BaseGeometry"""
        pass

    def area(self):
        """Computes the area of the geometry"""
        raise Exception('area() is not implemented')
