import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    if __name__ == "__main__":
        unittest.main()