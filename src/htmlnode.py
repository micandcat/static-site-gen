class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("method not implemented for base class")

    def props_to_html(self):
        result = ''
        if self.props is None or len(self.props) == 0 :
            return result
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result
        
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required")
        if self.tag is None:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        if not self.children:
            raise ValueError("ParentNode must have children")
        result = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            result += child.to_html()
        return result + f'</{self.tag}>'


