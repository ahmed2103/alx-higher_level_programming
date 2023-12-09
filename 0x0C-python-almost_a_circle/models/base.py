#!/usr/bin/python3

"""Module representing the Base class"""

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class variables"""
        Base.__nb_objects += 1
        self.id = id if id is not None else Base