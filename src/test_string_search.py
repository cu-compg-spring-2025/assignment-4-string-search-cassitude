import unittest
from naive_search import naive_search
from boyer_moore import boyer_moore_search


class TestStringSearch(unittest.TestCase):
    def test_string_search(self):
        self.assertEqual(naive_search("abc", "abc"), [0])
        self.assertEqual(naive_search("abcabc", "abc"), [0, 3])
        self.assertEqual(naive_search("abc", "bc"), [1])
        self.assertEqual(naive_search("abc", "c"), [2])
        self.assertEqual(naive_search("abc", "x"), [])
        self.assertEqual(naive_search("abccdebcb", "bc"), [1, 6])

        self.assertEqual(boyer_moore_search("abc", "abc"), [0])
        self.assertEqual(boyer_moore_search("abcabc", "abc"), [0, 3])
        self.assertEqual(boyer_moore_search("abc", "bc"), [1])
        self.assertEqual(boyer_moore_search("abc", "c"), [2])
        self.assertEqual(boyer_moore_search("abc", "x"), [])
        self.assertEqual(boyer_moore_search("abccdebcb", "bc"), [1, 6])


if __name__ == "__main__":
    unittest.main()
