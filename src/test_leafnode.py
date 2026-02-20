import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), '<h1>Hello, world!</h1>')

    def test_leaf_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    if __name__ == "__main__":
        unittest.main()

