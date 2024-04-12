import sys
import unittest
from main import prime_checker

class TestPrimeChecker(unittest.TestCase):
    def test_prime_checker(self):
        self.assertEqual(prime_checker(17), 0)
        self.assertEqual(prime_checker(4), 1)
        self.assertEqual(prime_checker(2), 0)
        self.assertEqual(prime_checker(0), 1)
        self.assertEqual(prime_checker("abc"), 1)
        self.assertFalse(prime_checker(17) == 1)

if __name__ == '__main__':
    unittest.main()