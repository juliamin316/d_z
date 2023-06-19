import unittest

class AnagramTest(unittest.TestCase):
    def test_find_anagrams(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        self.assertEqual(find_anagrams(words), expected_output)

if __name__ == '__main__':
    unittest.main()
