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
        nodes_array.append(TextNode(string_array[0], "text"))
        nodes_array.append(TextNode(string_array[1], text_type))
        nodes_array.append(TextNode(string_array[2], "text"))
    return nodes_array

def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    print(new_nodes)

main()
