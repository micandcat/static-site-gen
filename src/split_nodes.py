import re
from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text
        after = ''
        matches = extract_markdown_images(remaining)
        for match in matches:
            split = remaining.split(f'![{match[0]}]({match[1]})', 1)
            before = split[0]
            if len(split) > 1:
                after = split[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if len(split) > 1:
                remaining = after
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text
        after = ''
        matches = extract_markdown_links(remaining)
        for match in matches:
            split = remaining.split(f'[{match[0]}]({match[1]})', 1)
            before = split[0]
            if len(split) > 1:
                after = split[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if len(split) > 1:
                remaining = after
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes
