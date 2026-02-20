import unittest
from block import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Title"), BlockType.HEADING)
    
    def test_heading2(self):
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

def test_code(self):
    block = "```\nthis is code\n```"
    self.assertEqual(block_to_block_type(block), BlockType.CODE)

def test_quote(self):
    block = "> this\n> is\n> a quote"
    self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

def test_ul(self):
    block = "- this\n- is\n- an unordered list"
    self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

def test_ol(self):
    block = "1. this\n2. is an\n3. ordered list"
    self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    if __name__ == "__main__":
        unittest.main()