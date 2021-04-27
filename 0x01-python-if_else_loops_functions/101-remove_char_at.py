#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for index, letter in enumerate(str):
        if index != n:
            new += letter
    return new
