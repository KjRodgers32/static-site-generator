from inline_markdown_functions import *

def main():
    text = "Check out this ![cool image](https://i.imgur.com/fJRm4Vk.jpeg), followed by a `code example`, some *italicized words*, and finally a **bold statement** with a [useful link](https://boot.dev)."
    text_two = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) just some text at the end", "text")
    print(text_to_textnodes(text))

if __name__ == "__main__":
    main()
