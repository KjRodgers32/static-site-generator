import re
from LeafNode import LeafNode
from TextNode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode is invalid")
    
def split_nodes_delimiter(old_nodes ,delimiter, text_type):
    nodes_array = []
    for node in old_nodes:
        string_array = node.text.split(delimiter)
        if string_array[0] != '':
            nodes_array.append(TextNode(string_array[0], "text"))
        nodes_array.append(TextNode(string_array[1], text_type))
        if string_array[2] != '':
            nodes_array.append(TextNode(string_array[2], "text"))
    return nodes_array

def extract_markdown_images(text):
    alt_text_pattern = r"!\[(.*?)\]"
    print(re.findall(alt_text_pattern, text))

def extract_markdown_links(text):
    pass

def main():
    extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

main()
