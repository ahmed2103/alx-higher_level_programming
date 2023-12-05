#!/usr/bin/python3

"""
module defines a function that writes an object to 
a text file using a JSON representation
"""
def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    :param my_obj: The object to be written to the file.
    :type my_obj: Any
    :param filename: The name of the file to write to.
    :type filename: str
    :return: None
    """
    from json import dumps
    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
