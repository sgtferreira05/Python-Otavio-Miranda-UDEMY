# os + shutil - move, copy and delete files
# move/rename -> shutil.move
# move/rename -> os.rename
# copy -> shutil.copy
# delete -> os.unlink
# delete directory recursively -> shutil.rmtree



# os + shutil - copying files with Python
# Copy -> shutil.copy
    # 1. Copying files from one folder to another

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
MAIN_FOLDER = os.path.join(DESKTOP, 'EXEMPLO')
NEW_FOLDER = os.path.join(DESKTOP, 'NEW_FOLDER')

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(MAIN_FOLDER):
    for dir_ in dirs:
        new_path_dir = os.path.join(
            root.replace(MAIN_FOLDER, NEW_FOLDER), dir_
        )
        os.makedirs(new_path_dir, exist_ok=True)


    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(MAIN_FOLDER, NEW_FOLDER), file
        )
        shutil.copy(file_path, new_file_path)
