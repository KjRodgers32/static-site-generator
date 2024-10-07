import unittest
from block_markdown_functions import *

class TestBlockMarkdownFunctions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(["# This is a heading", 
                          "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
                          "* This is the first list item in a list block",
                          "* This is a list item",
                          "* This is another list item"], markdown_to_blocks(markdown))

    def test_block_to_block_type_heading(self):
        markdown_string = "# This is a heading"
        self.assertEqual("heading", block_to_block_type(markdown_string))

    def test_block_to_block_type_code(self):
        markdown_string = "```This is a block of code```"
        self.assertEqual("code", block_to_block_type(markdown_string))

    def test_block_to_block_type_quote(self):
        markdown_string = "> This is a quote"
        self.assertEqual("quote", block_to_block_type(markdown_string))

    def test_block_to_block_type_unordered_list_asterick(self):
        markdown_string = "* This is an unordered list"
        self.assertEqual("unordered list", block_to_block_type(markdown_string))

    def test_block_to_block_type_unordered_list_dash(self):
        markdown_string = "- This is an unordered list"
        self.assertEqual("unordered list", block_to_block_type(markdown_string))

    def test_block_to_block_type_ordered_list_one(self):
        markdown_string = "1. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))

    def test_block_to_block_type_ordered_list_two(self):
        markdown_string = "2. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_three(self):
        markdown_string = "3. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_four(self):
        markdown_string = "4. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_five(self):
        markdown_string = "5. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_six(self):
        markdown_string = "6. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_seven(self):
        markdown_string = "7. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_eight(self):
        markdown_string = "8. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))


    def test_block_to_block_type_ordered_list_nine(self):
        markdown_string = "9. This is an ordered list"
        self.assertEqual("ordered list", block_to_block_type(markdown_string))



if __name__ == "__main__":
    unittest.main()
