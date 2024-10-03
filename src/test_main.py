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
    
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertEqual([TextNode("This is text with a ", "text"),TextNode("code block", "code"),TextNode(" word", "text")], split_nodes_delimiter([node], "`", "code"))

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", "bold")
        self.assertEqual([TextNode("This is text with a ", "text"),TextNode("bolded phrase", "bold"),TextNode(" in the middle", "text")], split_nodes_delimiter([node], "**", "bold"))

    def test_split_nodes_delimiter_italics(self):
        node = TextNode("This is an *italic* and cool word.", "italic")
        self.assertEqual([TextNode("This is an ", "text"),TextNode("italic", "italic"),TextNode(" and cool word.", "text")], split_nodes_delimiter([node], "*", "italic"))
    
    def test_split_nodes_delimiter_at_begining(self):
        node = TextNode("**This is bold** from the very start", "bold")
        self.assertEqual([TextNode("This is bold", "bold"),TextNode(" from the very start", "text")], split_nodes_delimiter([node], "**", "bold"))
    
    def test_split_nodes_delimiter_at_end(self):
        node = TextNode("The code is at the very end: `code block`", "code")
        self.assertEqual([TextNode("The code is at the very end: ", "text"),TextNode("code block", "code")], split_nodes_delimiter([node], "`", "code"))
    
    def test_split_nodes_delimiter_the_entire_string(self):
        node = TextNode("*This entire line is italics*", "italic")
        self.assertEqual([TextNode("This entire line is italics", "italic")],split_nodes_delimiter([node], "*", "italic"))
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extract_markdown_links(text))

if __name__ == '__main__':
    unittest.main()
