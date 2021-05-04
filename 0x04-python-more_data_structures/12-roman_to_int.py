#!/usr/bin/python3
def roman_to_int(roman_string):
   if (type(roman_string) != str) or roman_string is None:
        return 0
    romannumbers = {'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev, sum = 0, 0
    for letter in roman_string:
        sum += romannumbers[letter] if romannumbers[letter] <= prev else romannumbers[letter] - prev * 2
        prev = romannumbers[letter]
    return sum

