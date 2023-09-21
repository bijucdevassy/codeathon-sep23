import unittest
from datascience_utils import sort_string_by_frequency

class TestSortStringByFrequency(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(sort_string_by_frequency(''), '')
    
    def test_single_character_string(self):
        self.assertEqual(sort_string_by_frequency('a'), 'a')
    
    def test_sorted_string(self):
        self.assertEqual(sort_string_by_frequency('aaabbbccc'), 'aaabbbccc')
    
    def test_unsorted_string(self):
        self.assertEqual(sort_string_by_frequency('cbacba'), 'ccbaab')
    
    def test_string_with_spaces(self):
        self.assertEqual(sort_string_by_frequency('a a b b c c'), 'aabbcc ')
    
if __name__ == '__main__':
    unittest.main()
