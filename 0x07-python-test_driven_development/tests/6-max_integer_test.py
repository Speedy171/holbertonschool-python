#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Testing for max integer"""

    def test_empty_list(self):
        """Testing for an empty list"""
        self.assertEqual(max_integer(), None)

    def test_list_of_positive_integers(self):
        """Testing for positive integers"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_list_of_negative_integers(self):
        """Testing for negative integers"""
        self.assertEqual(max_integer([-1, -5, -4]), -1)

    def test_list_with_1_element(self):
        """Testing for 1 integers"""
        self.assertEqual(max_integer([5]), 5)

    def test_list_with_positive_and_negative_elements(self):
        """Testing for positive and negative integers"""
        self.assertEqual(max_integer([-1,5,-7,20]), 20)

    def test_list_of_duplicate_elements(self):
        """Testing for duplicate values"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

if __name__ == '__main__':
        unittest.main()