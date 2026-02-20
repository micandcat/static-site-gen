import os
import sys
import shutil
from copy_dir import copy_dir
from generate_page import generate_page_recursive



def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    src = "static"
    dest = "docs"
    shutil.rmtree(dest)
    os.mkdir(dest)
    copy_dir(src, dest)

    generate_page_recursive("content", "template.html", "docs", basepath)

 

main()
