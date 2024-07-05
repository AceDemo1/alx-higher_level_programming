#!/usr/bin/python3
""" Module containing function find_peak """


def find_peak(list_of_integers):
    """Finction that  finds a peak in a list of unsorted integers."""
    begining = 0
    mid = 0
    end = len(list_of_integers) - 1
    if end > 0:
        while begining < end:
            mid = begining + (end - begining) // 2
            if (list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]):
                return list_of_integers[mid]
            if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
                end = mid
            else:
                begining = mid + 1
        return list_of_integers[begining]

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
