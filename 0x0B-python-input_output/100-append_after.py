#!/usr/bin/python3
"""appending function in module"""
def append_after(filename="", search_string="", new_string=""):
    """
    Append string function
    :param filename: Name of file to append to
    :type filename: str
    :param search_string: Key to find
    :type search_string: str
    :param new_string: String to append
    :type new_string: str
    :return: None
    """
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
              
