import unittest
from isUnique import is_unique


class TestIsUnique(unittest.TestCase):
    def test_true(self):
        str_true = "abcde"

        self.assertIs(is_unique(str_true), True)

    def test_false(self):
        str_false = "abcded"
        self.assertIs(is_unique(str_false), False)


if __name__ == '__main__':
    unittest.main()
