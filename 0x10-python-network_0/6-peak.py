#!/usr/bin/python3

"""Script that contain a function to get max int of an unsorted list"""

def find_peak(list_of_integers):
    """function to get max int inspired from binary search not actually"""

    if not list_of_integers:
        return None
    
    right = len(list_of_integers) - 1 #everything starts from zeroo
    left = 0
    
    while right > left:
        mid = (right + left) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]

