#!/usr/bin/python3
def read_file(filename=""):
    """Read the contents of a file in utf-8 encoding and print to stdout.

    Args:
        filename (str): The file to open and read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
