#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_max1(self):
        self.assertEqual(max_integer([1, 1]), 1)

    def test_max_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'i'])

