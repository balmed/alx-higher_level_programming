#!/usr/bin/python3
""" define module of class dirved or subclass"""
class MyList(list):
    def print_sorted(self):
        print(sorted(self))
