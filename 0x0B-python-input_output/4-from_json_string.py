#!/usr/bin/python3

"""module defines a function that desarializes a JSON string"""

def from_json_string(my_str):
    """
    Converts a JSON string representation into its corresponding Python object.

    :param my_str: A string containing a JSON representation.
    :type my_str: str
    :return: The Python object corresponding to the JSON string.
    :rtype: Any
    """
    from json import loads
    return loads(my_str) 
