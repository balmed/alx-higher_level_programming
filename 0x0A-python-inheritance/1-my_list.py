#!/usr/bin/python3
""" Module of class dirved or subclass"""
class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
