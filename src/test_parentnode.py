from typing import Union
import unittest
from ParentNode import ParentNode
from LeafNode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_pass_value_argument(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, ParentNode(tag="a", value="This should cause an error", children=["HTML Node", "HTML Node"]))
    
    def test_no_children_argument(self):
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, ParentNode(tag="a"))

    def test_to_html_tag_equal_None(self):
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError("Parent Node must have a tag"), ParentNode(tag=None, children=["Html Node", "Html Node"]).to_html())

    def test_to_html_tag_equal_empty_string(self):
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError("Parent Node must have a tag"), ParentNode(tag='  ', children=["Html Node", "Html Node"]).to_html())

    def test_to_html_no_props(self):
        parent_node = ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", parent_node.to_html())

    def test_to_html_with_prop_and_nested_parent(self):
        parent_node = ParentNode("div", 
                    [
                    ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("a", "Click This", {"href": "google.com"}),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )])
        self.assertEqual('<div><p><b>Bold text</b><a href="google.com">Click This</a>Normal text<i>italic text</i>Normal text</p></div>', parent_node.to_html())


    def test_to_html_with_prop_and_multiple_nested_parent(self):
        parent_node = ParentNode("div", 
                    [
                    ParentNode("div",
                    [ 
                    ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("a", "Click This", {"href": "google.com"}),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                               )], {"class": "this-is-a-class"})])
        self.assertEqual('<div><div class="this-is-a-class"><p><b>Bold text</b><a href="google.com">Click This</a>Normal text<i>italic text</i>Normal text</p></div></div>', parent_node.to_html())

    def test_to_html_with_multiple_props_and_multiple_nested_parent(self):
        parent_node = ParentNode("div", 
                    [
                    ParentNode("div",
                    [ 
                    ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode("a", "Click This", {"href": "google.com"}),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                               )], {"class": "this-is-a-class"})], {"class": "this-is-another-class"})
        self.assertEqual('<div class="this-is-another-class"><div class="this-is-a-class"><p><b>Bold text</b><a href="google.com">Click This</a>Normal text<i>italic text</i>Normal text</p></div></div>', parent_node.to_html())

