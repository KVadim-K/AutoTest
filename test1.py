import unittest
from main1 import divide, check

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

class TestMath(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertFalse(check(1))
        self.assertTrue(check(10))

        self.assertFalse(not check(2))
        self.assertTrue(not check(3))
        self.assertTrue(not check(51))

if __name__ == '__main__':
    unittest.main()





