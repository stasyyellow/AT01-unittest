import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(25, 7), 4)
        self.assertEqual(remainder(100, 10), 0)

    # Тест деления на 0
    def test_remainder_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

if __name__ == '__main__':
    unittest.main()
