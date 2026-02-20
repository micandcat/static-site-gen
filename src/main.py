import os
import shutil
from copy_dir import copy_dir
from generate_page import generate_page_recursive

def main():

    src = "static"
    dest = "public"
    shutil.rmtree(dest)
    os.mkdir(dest)
    copy_dir(src, dest)

    generate_page_recursive("content", "template.html", "public")

main()
