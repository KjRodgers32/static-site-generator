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
        if node.text_type != "text":
            nodes_array.append(node)
            continue
        split_nodes = []
        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise ValueError("This is not a valid markdown expression")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], "text"))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        nodes_array.extend(split_nodes)

    return nodes_array

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            text_nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            text_nodes.append(node)
            continue

        for link in links:
            splits = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splits) != 2:
                raise ValueError("This is an invalid markdown expression")
            if splits[0] != "":
                text_nodes.append(TextNode(splits[0], "text"))
            text_nodes.append(TextNode(link[0], "link", link[1]))
            text = splits[1]
        if text != "":
            text_nodes.append(TextNode(text, "text"))

    return text_nodes

def split_nodes_image(old_nodes):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            text_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            text_nodes.append(node)
            continue

        for image in images:
            splits = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splits) != 2:
                raise ValueError("This is an invalid markdown expression")
            if splits[0] != "":
                text_nodes.append(TextNode(splits[0], "text"))
            text_nodes.append(TextNode(image[0], "image", image[1]))
            text = splits[1]
        if text != "":
            text_nodes.append(TextNode(text, "text"))

    return text_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def main():
    text = "Check out this ![cool image](https://i.imgur.com/fJRm4Vk.jpeg), followed by a `code example`, some *italicized words*, and finally a **bold statement** with a [useful link](https://boot.dev)."
    text_two = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) just some text at the end", "text")
    print(text_to_textnodes(text))
if __name__ == "__main__":
    main()
