import unittest
from HtmlNode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_tag_default(self):
        html_node = HtmlNode(value="This is a value", children=["HTML Node", "HTML Node", "HTML Node"], props={"href": "https://www.google.com"})
        self.assertEqual(html_node.tag, None)

    def test_value_default(self):
        html_node = HtmlNode(tag="a", children=["HTML Node", "HTML Node", "HTML Node"], props={"href": "https://www.google.com"})
        self.assertEqual(html_node.value, None)

    def test_children_default(self):
        html_node = HtmlNode(value="This is a value", tag="p", props={"href": "https://www.google.com"})
        self.assertEqual(html_node.children, None)

    def test_props_default(self):
        html_node = HtmlNode(value="This is a value", children=["HTML Node", "HTML Node", "HTML Node"], tag="h1")
        self.assertEqual(html_node.props, None)

    def test_to_html_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            html_node = HtmlNode(tag="a", value="This is a value", children=["HTML Node", "HTML Node", "HTML Node"], props={"href": "https://www.google.com"})
            self.assertRegex(NotImplementedError, html_node.to_html())
    
    def test_props_to_html(self):
        html_node = HtmlNode(tag="a", value="This is a value", children=["HTML Node", "HTML Node", "HTML Node"], props={"href": "https://www.google.com"})
        html_node_two = HtmlNode(tag="a", value="This is a value", children=["HTML Node", "HTML Node", "HTML Node"], props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com"')
        self.assertEqual(html_node_two.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main() 