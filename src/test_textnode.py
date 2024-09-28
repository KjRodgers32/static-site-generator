import unittest

from TextNode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual(node1, node2)
    
    def test_eq_text_not_equal(self):
        node1 = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a new text node", "bold", "google.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_text_type_not_equal(self):
        node1 = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "italics", "google.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_url_not_equal(self):
        node1 = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "bing.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq_missing_requirement(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, TextNode("bold", "google.com"))

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual(print('TestNode(This is a text node, bold, google.com)'), print(node))

if __name__ == "__main__":
    unittest.main()