import unittest
a = 5
b = 5
c = 5

def classify_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or a == c or b == c:
        return "Isosceles"
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return "Right"
    return "Scalene"
    
def runclassify_triangle(a,b,c):

    result = classify_triangle(a,b,c)

    print(f"The triangle is {result} with sides {a}, {b} and {c}")

class testtriangles(unittest.TestCase):

    def test_not_triangle(self):
        result = classify_triangle(1, 2, 4)  # Example of a non-triangle
        self.assertEqual(result, "Not a triangle")

    def test_equilateral(self):
        result = classify_triangle(5, 5, 5)  # Example of an equilateral triangle
        self.assertEqual(result, "Equilateral")

    def test_isosceles(self):
        result = classify_triangle(5, 5, 7)  # Example of an isosceles triangle
        self.assertEqual(result, "Isosceles")

    def test_right(self):
        result = classify_triangle(3, 4, 5)  # Example of a right triangle
        self.assertEqual(result, "Right")

    def test_scalene(self):
        result = classify_triangle(3, 4, 6)  # Example of a scalene triangle
        self.assertEqual(result, "Scalene")

if __name__ == "__main__":
    unittest.main()