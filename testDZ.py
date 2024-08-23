import unittest
from DZ1 import remainder

class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 3), 1)  # 10 % 3 = 1
        self.assertEqual(remainder(20, 4), 0)  # 20 % 4 = 0
        self.assertEqual(remainder(15, 6), 3)  # 15 % 6 = 3

    def test_remainder_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(6, 0)

if __name__ == '__main__':
    unittest.main()
