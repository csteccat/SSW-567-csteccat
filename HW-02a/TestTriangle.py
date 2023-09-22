# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', 'Side greater than 200 should be InvalidInput')
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', 'Side less than or equal to 0 should be InvalidInput')
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', 'Floating-point numbers should be InvalidInput')
    
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 cannot form a triangle')
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1,1,2 cannot form a triangle')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 is a Scalene triangle')
        self.assertEqual(classifyTriangle(8, 6, 10), 'Scalene', '8,6,10 is a Scalene triangle')
    
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5,8,5 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8,5,5 is an Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

