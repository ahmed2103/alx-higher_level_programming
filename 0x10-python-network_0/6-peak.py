#!/usr/bin/python3

def find_peak(list_of_integers):
    """Function to find a peak in an unsorted list using binary search-inspired approach"""
    
    if not list_of_integers:
        return None
    
    right = len(list_of_integers) - 1
    left = 0
    
    while right < left:
        mid = (right + left) // 2
        
        if mid + 1 < len(list_of_integers) and list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return list_of_integers[left]
