import unittest
from 6-max_integer import max_integer

class TestMax(unittest.TestCase):
        def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)
if __name__ == "__main__":
    unittest.main()
