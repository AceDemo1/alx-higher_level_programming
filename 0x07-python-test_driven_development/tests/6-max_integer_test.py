#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_max1(self):
        self.assertEqual(max_integer([3, 2]), 3)

    def test_max2(self):
        self.assertEqual(max_integer([1, 1]), 1)

    def test_max3(self):
        self.assertEqual(max_integer([1, 2, 0]), 2)

    def test_max4(self):
        self.assertEqual(max_integer([-1, 2]), 2)

    def test_max5(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_max6(self):
        self.assertEqual(max_integer([-3, -2]), -2)

    def test_max7(self):
        self.assertEqual(max_integer([2]), 2)

    def test_max8(self):
        self.assertNone(max_integer([]))

    def test_max_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'i'])

