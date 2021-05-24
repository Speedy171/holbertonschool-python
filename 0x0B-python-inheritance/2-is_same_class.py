#!/usr/bin/python3

"""
is_same_class checks that obj is of the type a_class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the class"""
    return type(obj) == a_class
