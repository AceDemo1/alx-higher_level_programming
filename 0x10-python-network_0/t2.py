#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if the mid element is greater than the next element
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak is on the left side or it is the mid element
            high = mid
        else:
            # Peak is on the right side
            low = mid + 1

    return list_of_integers[low]

# Example usage:
array = [5, 4, 3, 2, 1]
peak = find_peak(array)
print(peak)  # Expected output is 5

