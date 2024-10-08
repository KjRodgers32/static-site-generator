import unittest
from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_children_argument(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError,LeafNode(tag="a", value="Click Me", children=["HTML Node", "HTML Node"], props={"href": "google.com"}))
    
    def test_no_value_argument(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError,LeafNode(tag="a", props={"href": "google.com"}).to_html())

    def test_no_tag_argument(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError,LeafNode(value="This is a value", props={"href": "google.com"}).to_html())

    def test_to_html_value_equal_none(self):
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError("Leaf Node must have a value!"),LeafNode(tag="a", value=None, props={"href": "google.com"}).to_html())

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(tag=None, value="Click")
        self.assertEqual("Click", leaf_node.to_html())

    def test_to_html_no_props(self):
        leaf_node = LeafNode(tag="p", value="This is a paragraph")
        self.assertEqual("<p>This is a paragraph</p>", leaf_node.to_html())

    def test_to_html(self):
        leaf_node = LeafNode(tag="a", value="Click Me", props={"href": "google.com"})
        self.assertEqual('<a href="google.com">Click Me</a>', leaf_node.to_html())


if __name__ == "__main__":
    unittest.main()
