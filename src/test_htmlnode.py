import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
                'a',
                'google',
                None,
                {"href": "https://www.google.com", "target": "_blank"}
        )
        print(node)

    def test_props(self):
        node = HTMLNode(
                'a',
                'google',
                None,
                {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_repr2(self):
        node = HTMLNode(
                'p',
                'this is a paragraph',
                ['1', '2', '3'],
                
        )
        print(node)

    if __name__ == "__main__":
        unittest.main()
