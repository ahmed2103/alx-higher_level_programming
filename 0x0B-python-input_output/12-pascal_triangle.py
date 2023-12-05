#!usr/bin/python3

"""module return nums of pascal triangle"""

def pascal_triangle(n):
   """
    function that returns a list of lists of integers

    :param n: integer number limit
    :type n: int
    :return: list of lists of integers representing the pascal triangle
    :rtype: list
    """
    pascal = []
    prev = []
    for i in range(n):
        curr = [1] + [sum(prev[j:j + 2]) for j in range(len(prev) - 1)]
        if i > 0:
            curr = curr + [1]
        pascal.append(curr)
        prev = curr
    return pascal
