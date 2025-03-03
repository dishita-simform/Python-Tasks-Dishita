import unittest

from Dishita_Python_Anagram import group_anagrams

class TestGroupAnagrams(unittest.TestCase):

    def test_group_anagrams(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
        
        self.assertEqual(group_anagrams([""]), [[""]])  # Edge case: empty string
        self.assertEqual(group_anagrams(["a"]), [["a"]])  # Edge case: single letter
        self.assertEqual(group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]),
                         [["abc", "bca", "cab"], ["xyz", "zyx"]])  # Multiple anagram groups
        self.assertEqual(group_anagrams([]), [])  # Edge case: empty list

if __name__ == "__main__":
    unittest.main()
