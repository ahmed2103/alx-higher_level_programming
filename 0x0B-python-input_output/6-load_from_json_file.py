#!/usr/bin/python3

"""module loads object from json file"""
def load_from_json_file(file_path):
    """
    Loads data from a JSON file and returns the corresponding Python object.

    :param file_path: The path to the JSON file.
    :type file_path: str
    :return: The Python object corresponding to the JSON data in the file.
    :rtype: Any
    """
    from json import load

    with open(file_path) as file:
        return load(file)
