#!/usr/bin/python3

"""Script that contains a function to find a peak in an unsorted list"""

def find_peak(list_of_integers):
    """Function to find a peak in a list of integers, inspired by binary search"""

    if list_of_integers is None or list_of_integers == []:
        return None
    
    left = 0
    right = len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]
