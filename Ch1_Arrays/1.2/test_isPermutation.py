import unittest
from isPermutation import is_permutation


class TestIsPermutation(unittest.TestCase):
    def is_perm_true(self):
        rats = "rats"
        star = "star"
        self.assertIs(is_permutation(rats, star), True)

    def is_perm_false(self):
        rats = "rats"
        stare = "stare"
        rate = "rate"
        self.assertIs(is_permutation(rats, stare), False)
        self.assertIs(is_permutation(rats, rate), False)
