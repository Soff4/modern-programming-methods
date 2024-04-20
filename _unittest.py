import unittest
from main import Singleton

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        instance_01 = Singleton(42)
        instance_02 = Singleton(24)

        self.assertEqual(instance_01.value, 42)
        self.assertEqual(instance_02.value, 42)
        self.assertIs(instance_01, instance_02)

if __name__ == '__main__':
    unittest.main()