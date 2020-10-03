import unittest
from isUnique import is_unique


class TestIsUnique(unittest.TestCase):
    def test_true(self):
        str_true = "abcde"
        str_space = " "
        self.assertIs(is_unique(str_true), True)
        self.assertIs(is_unique(str_space), True)

    def test_false(self):
        str_false = "abcded"
        str_space = "  "
        self.assertIs(is_unique(str_false), False)
        self.assertIs(is_unique(str_space), False)


if __name__ == '__main__':
    unittest.main()
