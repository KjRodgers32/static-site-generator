import unittest
from main import *
from TextNode import TextNode

class TestMainFunctions(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("My name is Kevin", "text", None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual("My name is Kevin", leaf_node.to_html())

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("My name is Kevin", "bold", None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual("<b>My name is Kevin</b>", leaf_node.to_html())

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("My name is Kevin", "italic", None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual("<i>My name is Kevin</i>", leaf_node.to_html())

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("My name is Kevin", "code", None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual("<code>My name is Kevin</code>", leaf_node.to_html())

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("My name is Kevin", "link", "kevin.com")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual('<a href="kevin.com">My name is Kevin</a>', leaf_node.to_html())

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("My name is Kevin", "image", "kevin.com")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual('<img src="kevin.com" alt="My name is Kevin"></img>', leaf_node.to_html())

    def test_text_node_to_html_node_invalid(self):
        with self.assertRaises(Exception):
            text_node = TextNode("My name is Kevin", "invlaid-type", "kevin.com")
            self.assertRaises(Exception, text_node_to_html_node(text_node))

if __name__ == '__main__':
    unittest.main()
