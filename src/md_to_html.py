from md_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
import textwrap

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_children = []

    for block in blocks:
        if not block.strip():
            continue
        type = block_to_block_type(block)
        #based on type, create HTMLNode with proper data
        #HTMLNode takes tag, value, children, props, all optional
        #paragraph, heading, code, quote, un- and ordered list
        if type == BlockType.PARAGRAPH:
            #tag is <p>, but need to replace \n with " "
            text = " ".join(line.strip() for line in block.splitlines())
            node = ParentNode("p", text_to_children(text))
        elif type == BlockType.HEADING:
            # need to determine if tag is h1 - h6, need to remove md tag
            n = get_h_num(block)
            text = block[n:].lstrip()
            node = ParentNode(f"h{n}", text_to_children(text))
        elif type == BlockType.CODE:
            # need to remove md tag from text but preserve any other inline md tags
            lines = block.splitlines()
            text = "\n".join(lines[1:-1]) 
            text = textwrap.dedent(text) + "\n"
            code = ParentNode("code", [LeafNode(None, text)])
            node = ParentNode("pre", [code])
            
        elif type == BlockType.QUOTE:
            #render text without md tag
            lines = block.splitlines()
            stripped = []
            for line in lines:
                if line.startswith("> "):
                    stripped.append(line[2:])
                elif line.startswith(">"):
                    stripped.append(line[1:])
                else:
                    stripped.append(line)
            text = "\n".join(stripped)
            node = ParentNode("blockquote", text_to_children(text))

        elif type == BlockType.UNORDERED_LIST:
            #render text without md tag, and children need <li> tag
            lines = block.splitlines()
            children = []
            for line in lines:
                if line.startswith("- ") or line.startswith("* "):
                    text = line[2:]
                else:
                    text = line
                children.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ul", children)

        elif type == BlockType.ORDERED_LIST:
            #render text without markdown tag, and children need <li> tag
            lines = block.splitlines()
            children = []
            for line in lines:
                i = line.find(". ")
                text = line[i+2:] if i != -1 else line
                children.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ol", children)

        node_children.append(node)

    parent = ParentNode("div", node_children, None)
    return parent

def text_to_children(text):
    # takes text and returns list of HTMLNodes, uses text_node_to_html
    nodes = text_to_textnodes(text)
    if not nodes:
        return [LeafNode(None, "")]
    hnodes = []
    for node in nodes:
        hnodes.append(text_node_to_html_node(node))
    return hnodes

def get_h_num(block):
    count = 0
    for i in range(len(block[0:6])):
        if block[i] != '#':
            break
        count += 1
    return count