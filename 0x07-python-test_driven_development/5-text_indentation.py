#!/usr/bin/python3

"""
This module contains text_indentation function
"""


def text_indentation(text):
    """
    Prints text with two lines following every '?.:'
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    
    characters = ''
    for i in range(0, len(text)):
        character = text[i]
        characters += character
        if i == len(text) - 1:
            print(characters.strip(), end="")
        elif character in '?.:':
            print(characters.strip(), end="\n\n")
            characters = ''