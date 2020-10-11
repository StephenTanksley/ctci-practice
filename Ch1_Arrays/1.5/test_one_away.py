import unittest
from one_away import one_away


class TestOneAway(unittest.TestCase):
    def one_away_true(self):
        true_string1 = "pales"
        true_string2 = "pale"
        true_string3 = "pares"

        # Strings 2 and 3 are only 1 difference away from string 1.

        self.assertTrue(one_away(true_string1, true_string2))
        self.assertTrue(one_away(true_string1, true_string3))

    def one_away_false(self):
        false_string1 = "pales"
        false_string2 = "pal"
        false_string3 = "pore"

        self.assertFalse(one_away(false_string1, false_string2))
        self.assertFalse(one_away(false_string2, false_string3))


if __name__ == "__main__":
    unittest.main()
