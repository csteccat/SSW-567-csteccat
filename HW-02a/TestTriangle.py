# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_Triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classify_Triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_Triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_Triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    
    def testInvalidInput(self):
        self.assertEqual(classify_Triangle(201, 1, 1), 'InvalidInput', 'Side greater than 200 should be InvalidInput')
        self.assertEqual(classify_Triangle(0, 1, 1), 'InvalidInput', 'Side less than or equal to 0 should be InvalidInput')
        self.assertEqual(classify_Triangle(1.5, 2, 3), 'InvalidInput', 'Floating-point numbers should be InvalidInput')
    
    def testNotATriangle(self):
        self.assertEqual(classify_Triangle(1, 2, 3), 'NotATriangle', '1,2,3 cannot form a triangle')
        self.assertEqual(classify_Triangle(1, 1, 2), 'NotATriangle', '1,1,2 cannot form a triangle')

    def testScalene(self):
        self.assertEqual(classify_Triangle(3, 4, 6), 'Scalene', '3,4,6 is a Scalene triangle')
        self.assertEqual(classify__Triangle(5, 5, 8), 'Isosceles', '5,5,8 is an Isosceles triangle')
        self.assertEqual(classify_Triangle(5, 8, 5), 'Isosceles', '5,8,5 is an Isosceles triangle')
        self.assertEqual(classify_Triangle(8, 5, 5), 'Isosceles', '8,5,5 is an Isosceles triangle')

    def testBoundary(self):
        self.assertEqual(classify_Triangle(1, 1, 200), 'InvalidInput', 'Side greater than 200 should be InvalidInput')
        self.assertEqual(classify_Triangle(0, 1, 1), 'InvalidInput', 'Side less than or equal to 0 should be InvalidInput')
        self.assertEqual(classify_Triangle(0, 0, 0), 'InvalidInput', 'All sides should be greater than 0')
        
    def testNegative(self):
        self.assertEqual(classify_Triangle(-1, 2, 3), 'InvalidInput', 'Negative sides should be InvalidInput')
        self.assertEqual(classify_Triangle(2, -1, 3), 'InvalidInput', 'Negative sides should be InvalidInput')
        self.assertEqual(classify_Triangle(2, 3, -1), 'InvalidInput', 'Negative sides should be InvalidInput')

    def testValidValues(self):
        self.assertEqual(classify_Triangle(1e8, 1e8, 1e8), 'Equilateral', 'Large values should be Equilateral')
        self.assertEqual(classify_Triangle(1e8, 1e8, 2e8), 'Isosceles', 'Large values should be Isosceles')
        self.assertEqual(classify_Triangle(3e8, 4e8, 5e8), 'Right', 'Large values should be Right')

    def testingTriangles(self):
        self.assertEqual(classify_Triangle(7, 8, 9), 'Scalene', '7,8,9 is a Scalene triangle')
        self.assertEqual(classify_Triangle(5, 5, 7), 'Isosceles', '5,5,7 is an Isosceles triangle')
        self.assertEqual(classify_Triangle(9, 12, 15), 'Right', '9,12,15 is a Right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

