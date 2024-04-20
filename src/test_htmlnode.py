import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "hello", children=None, props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("HTMLNode(a, hello, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))
    
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            None,
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()