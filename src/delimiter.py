from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception("invalid Markdown syntax")
        if count == 0:
            new_nodes.append(node)
            continue
        split = node.text.split(delimiter)
        for i, part in enumerate(split):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
