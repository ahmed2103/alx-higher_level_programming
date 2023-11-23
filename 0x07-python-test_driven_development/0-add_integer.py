#!/usr/bin/python3
"""Function: add_integer

Description:
    This function performs addition of two numbers, 'a' and 'b', where 'b' defaults to 98 if not provided.

Returns:
    int: The sum of 'a' and 'b'.

Raises:
    TypeError: If 'a' or 'b' is not an integer or float.
"""

def add_integer(a, b=98):
    """Returns a + b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
