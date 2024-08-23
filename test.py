import unittest
from main import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertNotEqual(add(10, -5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertNotEqual(subtract(10, -5), 5)

    def test_multiply(self):
        self.assertNotEqual(multiply(10, 5), 55)
        self.assertEqual(multiply(10, -5), -50)

    def test_divide(self):
        self.assertEqual(divide(10, 8), 2)
        self.assertNotEqual(divide(10, -5), 2)

if __name__ == '__main__':
    unittest.main()
