#!/usr/bin/python3
"""Adds a new attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """Add a new attribute to the object if possible"""
    if '__slots__' in dir(obj) or '__dict__' not in dir(obj) or hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
