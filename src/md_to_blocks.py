
def markdown_to_blocks(markdown):
    blocks = []
    split = markdown.split("\n\n")
    for part in split:
        if part is None:
            continue
        blocks.append(part.strip())
    return blocks
