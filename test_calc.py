# CS362 test_calc
# Alex Young
# 2/4/2021
# Run this file using python3 test_calc.py
# This program holds funtions to unit test for the avg function in HW4

import unittest
import calc

class TestCube(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, -5), 0)
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(0, 3.2), 3.2)
        self.assertEqual(calc.add(2, "4"), "Type Error")
    def test_sub(self):
        self.assertEqual(calc.sub(5, -5), 10)
        self.assertEqual(calc.sub(2, 3), -1)
        self.assertEqual(calc.sub(2.5, 0), 2.5)
        self.assertEqual(calc.sub(2, "3"), "Type Error")
    def test_mul(self):
        self.assertEqual(calc.mul(0, 0), 0)
        self.assertEqual(calc.mul(5, 5), 25)
        self.assertEqual(calc.mul(5, -2.5), -12.5)
        self.assertEqual(calc.mul("5", -2.5), "Type Error")
    def test_div(self):
        self.assertEqual(calc.div(5, 0), "Zero Division")
        self.assertEqual(calc.div(5, 2.5), 2)
        self.assertEqual(calc.div(10, 2), 5)
        self.assertEqual(calc.div(-10, 2), -5)

if __name__ == '__main__':
    unittest.main(verbosity=2)