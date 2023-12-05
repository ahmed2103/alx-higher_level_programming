#!/usr/bin/python3

"""module loads object from json file"""

def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    :param filename: json file name
    :type filename: string
    :return: none
    """
    from json import load
    with open(filename) as f:
        return load(f.read())
