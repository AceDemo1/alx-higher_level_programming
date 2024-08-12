#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2
        
        # Move to the left half if the middle element is smaller than its left neighbor
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        else:
            low = mid

    return list_of_integers[low]

# Example usage:
array = [8, 9, 5, 6, 5, 1]
peak = find_peak(array)
print(peak)  # Expected output is 9

