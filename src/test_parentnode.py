import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_tags(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "Italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        )

    if __name__ == "__main__":
        unittest.main()

