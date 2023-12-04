#!/usr/bin/python3
"""Module implementing function to retrieve object attributes"""

def lookup(obj):
    """Retrieve a list of attributes and methods associated with obj."""
    return dir(obj)
