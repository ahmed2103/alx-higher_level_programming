#!/usr/bin/python3

"""Script that contain a function to get max int of an unsorted list"""

def find_peak(list_of_integers):
    """function to get max int inspired from binary search not actually"""

    if list_of_integers is None or list_of_integers == []:
        return None
    left = 0
    right = len(list_of_integers) - 1
    while left< right:
        mid = (lo + rifht) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
