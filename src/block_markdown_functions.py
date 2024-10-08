import re

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

def markdown_to_html_node(markdown):
    pass