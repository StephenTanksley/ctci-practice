import unittest
from URLify import urlify


class TestURLify(unittest.TestCase):
    def test_is_urlified(self):
        name_str = "Mr John Smith"
        name_url = "Mr%20John%20Smith"
        self.assertEqual(urlify(name_str), name_url)

    def test_no_change(self):
        name_str = "MrJacobJones"
        return_string = "MrJacobJones"
        self.assertEqual(urlify(name_str), return_string)


if __name__ == '__main__':
    unittest.main()
