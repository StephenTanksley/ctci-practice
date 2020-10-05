import unittest
from isPermutation import is_permutation


class TestIsPermutation(unittest.TestCase):
    def is_perm_true(self):
        rats = "rats"
        star = "star"
        arts = "arts"
        self.assertIs(is_permutation(rats, star), True)
        self.assertIs(is_permutation(arts, rats), True)

    def is_perm_false(self):
        rats = "rats"
        stare = "stare"
        rate = "rate"
        self.assertIs(is_permutation(rats, stare), False)
        self.assertIs(is_permutation(rats, rate), False)
        self.assertIs(is_permutation(rats, rats), False)


if __name__ == '__main__':
    unittest.main()
