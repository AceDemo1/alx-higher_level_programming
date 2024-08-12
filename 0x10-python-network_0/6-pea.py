#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2
        
        # If mid is greater than its left neighbor, move to the left half
        if mid > 0 and list_of_integers[mid] > list_of_integers[mid - 1]:
            high = mid  # Move to the left side by adjusting high
        # Otherwise, move to the right half
        else:
            low = mid + 1  # Move to the right side by adjusting low

    return list_of_integers[low]

