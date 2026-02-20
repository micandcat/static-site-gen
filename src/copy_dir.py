import os
import shutil

def copy_dir(src, dest):
    if not os.path.exists(src) or not os.path.exists(dest):
        raise Exception("source and/or destination must exist")


    if not os.path.isfile(src):
        src_list = os.listdir(src)
        for item in src_list:
            if os.path.isfile(os.path.join(src, item)):
                print(item)
                shutil.copy(os.path.join(src, item), dest)
            else:
                new_dest = os.path.join(dest, item)
                os.mkdir(new_dest)
                new_src = os.path.join(src, item)
                print(new_dest)
                print(new_src)
                copy_dir(new_src, new_dest)