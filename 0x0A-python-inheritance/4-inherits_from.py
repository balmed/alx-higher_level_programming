#!/usr/bin/python3
'''Module class method.'''


def inherits_from(obj, a_class):
    '''Determines if  object is a subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
