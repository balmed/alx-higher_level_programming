#!/usr/bin/python3
"""Finds the peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds the peak in an unsorted list of ints"""
    if len(list_of_integers) == 0:
        return None
    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak(lint, start, stop):
    """Recursively finds peak"""
    if start == stop:
        return lint[start]

    mid = (start + stop) // 2

    if lint[mid] >= lint[mid + 1]:
        return _find_peak(lint, start, mid)
    else:
        return _find_peak(lint, mid + 1, stop)
