#!/usr/bin/python3
"""
    3-say_my_name.py
    This module contains the following say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Print the following: "My name is <first name> <last name>"
    """
    if type(first_name) not in [str]:
        raise TypeError('first_name must be a string')
    if type(last_name) not in [str]:
        raise TypeError('last_name must be a string')
    if len(first_name.replace(' ', '')) == 0:
        raise ValueError('first name can\'t be empty')
    print("My name is {} {}".format(first_name, last_name))
