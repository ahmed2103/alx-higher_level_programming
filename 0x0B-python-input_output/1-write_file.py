#!/usr/bin/python3
"""Module to write text to a file"""

def write_file(filename="", text=""):
    """Write `text` to `filename` and return the number of characters written.

    Args:
        filename (str): The file to write to.
        text (str): The text to write into `filename`.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf8') as file:
        return file.write(text)
