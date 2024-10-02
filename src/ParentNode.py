from HtmlNode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag.strip() == '':
            raise ValueError("Parent Node must have a tag")
        if self.children == None:
            raise ValueError("Parent Node must have children")
        
        leaf_string = ''
        for leaf_node in self.children:
            leaf_string += leaf_node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{leaf_string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

