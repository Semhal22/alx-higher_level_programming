#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
A peak number is greater than both it's left and right side numbers
if they exist
"""


def find_peakRecur(arr, left, right, length):
    mid = int(left + (right - left) / 2)
    if ((mid == 0 or arr[mid] >= arr[mid - 1]) and
       (mid == length - 1 or arr[mid] >= arr[mid + 1])):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peakRecur(arr, left, mid - 1, length)

    else:
        return find_peakRecur(arr, mid + 1, right, length)


def find_peak(list_of_integers):
    """Function that finds the peak"""
    length = len(list_of_integers)
    if not length:
        return None
    index = find_peakRecur(list_of_integers, 0, length - 1, length)

    return list_of_integers[index]
