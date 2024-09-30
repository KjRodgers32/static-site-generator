from HtmlNode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node must have a value!")