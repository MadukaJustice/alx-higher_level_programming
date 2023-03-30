#!/usr/bin/python3
"""
    Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ Function def """

    arr = list_of_integers
    l_end = 0
    r_end = len(arr) - 1

    """ Test empty list """
    if len(arr) == 0:
        return None

    if arr[l_end] > arr[l_end+1]:
        return arr[l_end]
    if arr[r_end] > arr[r_end-1]:
        return arr[r_end]

    if (len(arr)) % 2 == 0:
        mid = ((l_end + r_end) // 2) + 1
    else:
        mid = (l_end + r_end) // 2

    if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
        return arr[mid]
    if arr[mid] < arr[mid-1]:
        return find_peak(arr[l_end:mid+1])
    elif arr[mid] < arr[mid+1]:
        return find_peak(arr[mid:r_end+1])
    else:
        return arr[l_end]
