#!/usr/bin/python3

"""module to seralize an object to JSON"""
def to_json_string(my_obj):

    """
    function to seralize an object to JSON.

    Args:
        my_obj: object to seralize

    Returns:
        dict: JSON representation of an object

    """
    from json import dumps
    return dumps(my_obj)
