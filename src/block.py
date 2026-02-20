from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    count = 0
    for i in range(len(block[0:6])):
        if block[i] != '#':
            break
        count += 1
    if 1 <= count <= 6 and len(block) > count:    
        if block[count] == " ":
            return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    if is_quote(lines):
        return BlockType.QUOTE
    if is_ul(lines):
        return BlockType.UNORDERED_LIST
    if is_ol(lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def is_quote(lines):
    result = False
    for line in lines:
        if line.startswith(">") or line.startswith("> "):
            result = True
        else:
            result = False
            break
    return result

def is_ul(lines):
    result = False
    for line in lines:
        if line.startswith("- "):
            result = True
        else:
            result = False
            break
    return result

def is_ol(lines):
    result = False
    num = 1
    for line in lines:
        if line.startswith(f"{num}. "):
            result = True
        else:
            result = False
            break
        num += 1
    return result