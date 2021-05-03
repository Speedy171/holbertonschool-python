#!/usr/bin/python3
def no_c(my_string):
    return ''.join(letter for letter in my_string if letter not in 'cC')
