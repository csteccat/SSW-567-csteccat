# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the triangle.

    return:
        - 'Equilateral' if all three sides are equal.
        - 'Isosceles' if exactly one pair of sides are equal.
        - 'Scalene' if no pair of sides are equal.
        - 'NotATriangle' if it's not a valid triangle.
        - 'Right' if the sum of any two sides equals the square of the third side.
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # the sum of any two sides must be strictly less than the third side for a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return 'Right'
    if a != b and b != c and a != c:
        return 'Scalene'

    return 'Isosceles'
