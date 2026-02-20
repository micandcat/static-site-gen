import os
import pathlib
from md_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="UTF-8") as f:
        from_data = f.read()
    
    with open(template_path, "r", encoding="UTF-8") as f:
        template_data = f.read()
    
    node = markdown_to_html_node(from_data)
    html = node.to_html()
    title = extract_title(from_data)

    replaced = template_data.replace("{{ Title }}", title)
    content = replaced.replace("{{ Content }}", html)
    href = content.replace('href="/', f'href="{basepath}')
    final = href.replace('src="/', f'src="{basepath}')

    dir_path = os.path.dirname(dest_path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="UTF-8") as f:
        f.write(final)
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    dir_list = os.listdir(dir_path_content)

    for item in dir_list:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, pathlib.Path(f"{dest_path[:-3]}.html"), basepath)
        else:
            generate_page_recursive(item_path, template_path, dest_path, basepath)
    
