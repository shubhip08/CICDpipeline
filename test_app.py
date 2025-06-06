import unittest
from app import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

if __name__ == '__main__':
    unittest.main()