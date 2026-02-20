from delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_list = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(text_list, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    node_list = split_nodes_link(image)
    return node_list
