#!usr/bin/python3

"""module return nums of pascal triangle"""

def pascal_triangle(n):
    """return nums of pascal triangle"""
    pascal = []
    prev = []
    for i in range(n):
        curr = [1] + [sum(prev[j:j + 2]) for j in range(len(prev) - 1)]
        if i > 0:
            curr = curr + [1]
        pascal.append(curr)
        prev = curr
    return pascal
