from HtmlNode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag=None, value=None, props=None,):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node must have a value!")
        if self.tag == None:
            return f"{self.value}"
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
