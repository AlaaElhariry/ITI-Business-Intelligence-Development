import unittest
from lab import reverse_string, count_letters, remove_duplicates

class TestStringFunctions(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("abc"), "cba")

    def test_count_letters(self):
        self.assertEqual(count_letters("abc123"), 3)
        self.assertEqual(count_letters("hello!"), 5)

    def test_remove_duplicates(self):
        self.assertEqual(set(remove_duplicates([1,2,2,3])), {1,2,3})


if __name__ == "__main__":
    unittest.main()