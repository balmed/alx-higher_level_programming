#!/usr/bin/python3
"""Finds the peak a unsorted list of integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return _find_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def _find_peak(l, st, sp):
    """Recursively  peak"""
    if sp - st < 2:
        return None
    mid = (st + sp) // 2
    if l[mid] >= l[mid - 1] and l[mid] >= l[mid + 1]:
        return l[mid]
    return _find_peak(l, st, mid) or _find_peak(l, mid, sp)
