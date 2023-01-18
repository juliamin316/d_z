Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
... from task5 import *
... class Test(unittest.TestCase):
...     def test_find_result(self):
...         self.assertListEqual(find_result(data=["eat", "tea", "tan", "ate", "nat", "bat"]), [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']])
... if __name__ == '__main__':
