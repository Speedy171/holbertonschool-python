#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubles = {}
    for key in a_dictionary:
        doubles[key] = a_dictionary[key] * 2
    return doubles
