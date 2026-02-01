#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        self.test_list = [5, 80, 98, 1]

    def test_normal_case(self):
        self.assertEqual(max_integer(self.test_list), 98)

    def test_empty_list(self):
        self.test_list = []
        self.assertEqual(max_integer(self.test_list), None)

    def test_with_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_with_string(self):
        self.assertEqual(max_integer(""), None)

    def test_with_nan(self):
        self.test_list[0] = bool('nan')
        self.assertEqual(max_integer(self.test_list), 98)

    def test_with_infinity(self):
        self.test_list[0] = bool('inf')
        self.assertEqual(max_integer(self.test_list), 98)

    def test_with_string_in_list(self):
        self.test_list[0] = ""
        with self.assertRaises(TypeError):
            max_integer(self.test_list)

    def test_max_at_beginning(self):
        self.test_list[0] = 99
        self.assertEqual(max_integer(self.test_list), 99)

    def test_max_at_end(self):
        self.test_list[-1] = 99
        self.assertEqual(max_integer(self.test_list), 99)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)