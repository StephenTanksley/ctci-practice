import unittest
from palindrome_permutation import palindrome_permutation


class TestPalindromePermutation(unittest.TestCase):
    def palindrome_permutation_true(self):
        taco_cat = "taco cat"
        a_man = "a man a plan a canal panama"

        self.assertTrue(palindrome_permutation(taco_cat))
        self.assertTrue(palindrome_permutation(a_man))

    def palindrome_permutation_false(self):
        taco_dog = "taco dog"
        a_man_bobby = "a man a plan a canal panama bobby"

        self.assertFalse(palindrome_permutation(taco_dog))
        self.assertFalse(palindrome_permutation(a_man_bobby))


if __name__ == '__main__':
    unittest.main()
