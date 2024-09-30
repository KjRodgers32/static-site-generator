import unittest
from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_not_allow_children_in_constuctor(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError,LeafNode(tag="a", value="Click Me", children=["HTML Node", "HTML Node"], props={"href": "google.com"}))
    
    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            leaf_node = LeafNode(tag="a", props={"href": "google.com"}) 
            self.assertRaises(ValueError("Leaf Node must have a value!"), leaf_node.to_html())


if __name__ == "__main__":
    unittest.main()