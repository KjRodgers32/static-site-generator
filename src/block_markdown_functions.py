import re

from HtmlNode import HtmlNode

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split('\n')
    return [x for x in markdown_blocks if x.strip() != ""]

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        return "heading"
    if markdown.startswith("```"):
        return "code"
    if markdown.startswith(">"):
        return "quote"
    if markdown.startswith("*") or markdown.startswith("-"):
        return "unordered list"
    if re.match(r"^[0-9]+\.", markdown):
        return "ordered list"
    else:
        return "paragraph"

def block_type_to_tag(block_type):
    match block_type:
        case "heading":
            return "h1"
        case "code":
            return "code"
        case "quote":
            return "blockquote"
        case "unordered list":
            return "ul"
        case "ordered list":
            return "ol"
        case "paragraph":
            return "p"
        case _:
            raise Exception("Invalid block type")

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for markdown in markdown_blocks:
        print(HtmlNode(block_type_to_tag(block_to_block_type(markdown)), markdown))

print(markdown_to_html_node("""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
))

