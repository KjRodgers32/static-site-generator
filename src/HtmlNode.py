class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ''
        length_of_props = len(self.props)
        for k, v in self.props.items():
            string += f'{k}="{v}"'
            if length_of_props > 1:
                string += ' '
                length_of_props -= 1
        return string