def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line[0:2] == "# ":
            return line[2:]
        else:
            continue
    raise Exception("no h1 header")