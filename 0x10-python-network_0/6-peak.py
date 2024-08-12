#!/usr/bin/python3
"""This module defines the function "find_peak" in a list
of unsorted integers"""

def find_peak(list_of_integers):
    """func"""
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        # If mid is greater than its left neighbor, move to the left half
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        # Otherwise, move to the right half
        else:
            low = mid + 1

    return list_of_integers[high]

