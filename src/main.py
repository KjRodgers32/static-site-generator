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
    image_link_pattern = r"\((.*?)\)"

    alt_text_array = re.findall(alt_text_pattern, text)
    image_link_array = re.findall(image_link_pattern, text)

    markdown_array = []

    for i in range(len(alt_text_array)):
        markdown_array.append((alt_text_array[i], image_link_array[i]))

    return markdown_array

def extract_markdown_links(text):
    alt_text_pattern = r"\[(.*?)\]"
    link_pattern = r"\((.*?)\)"

    alt_text_array = re.findall(alt_text_pattern, text)
    link_array = re.findall(link_pattern, text)

    markdown_array = []

    for i in range(len(alt_text_array)):
        markdown_array.append((alt_text_array[i], link_array[i]))

    return markdown_array

def split_nodes_link(old_nodes):
    text_nodes = []

    for node in old_nodes:
        text_split_array = re.split(r"\[(.*?)\]\(.*?\)", node.text)
        link_split_array = extract_markdown_links(node.text)

        for string in text_split_array:
            i = 0
            while i != len(link_split_array):
                if string == link_split_array[i][0]:
                    text_nodes.append(TextNode(string, "link", link_split_array[i][1])) 
                    break
                if string != link_split_array[i][0]:
                    i += 1
            if string.strip() != '' and i == len(link_split_array):
                text_nodes.append(TextNode(string, "text"))

    return text_nodes

def split_nodes_image(old_nodes):
    text_nodes = []

    for node in old_nodes:
        text_split_array = re.split(r"!\[(.*?)\]\(.*?\)", node.text)
        image_split_array = extract_markdown_images(node.text)

        for string in text_split_array:
            i = 0
            while i != len(image_split_array):
                if string == image_split_array[i][0]:
                    text_nodes.append(TextNode(string, "link", image_split_array[i][1])) 
                    break
                if string != image_split_array[i][0]:
                    i += 1
            if string.strip() != '' and i == len(image_split_array):
                text_nodes.append(TextNode(string, "text"))
    
    return text_nodes


def main():
    print(split_nodes_link([TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",
)]))
    
    print(split_nodes_image([TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        "text"
    )]))


if __name__ == "__main__":
    main()
