import sys
import unittest
from main import prime_checker

class TestPrimeChecker(unittest.TestCase):
    def test_prime_checker(self):
        with self.assertRaises(SystemExit) as cm:
            prime_checker(4)
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            prime_checker(17)
        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()