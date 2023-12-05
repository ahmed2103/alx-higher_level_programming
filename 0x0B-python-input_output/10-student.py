#!/usr/bin/python3
"""Module implementing class with method to serialize itself"""


class Student:
    """Class to represent student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new student instance first and last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Create dict of attributes for use in json string

        If `attrs` is not None, use `attrs` list to select desired attributes.
        """
        if attrs is None or not isinstance(attrs, (list)):
            return self.__dict__
        else:
            required = {k: v for k, v in filter(lambda x: x[0] in attrs,
                                           self.__dict__.items())}
            return required
