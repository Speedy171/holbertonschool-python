#!/usr/bin/python3

"""
is_kind_of_class Module returns true if obj is or inherits from a_class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the class, or an instance
    of the class that it has inherited from"""
    return isinstance(obj, a_class)
