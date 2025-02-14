# os + shutil - move, copy and delete files
# move/rename -> shutil.move
# move/rename -> os.rename
# copy -> shutil.copy
# delete files -> os.unlink
# delete directory recursively -> shutil.rmtree


import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
MAIN_FOLDER = os.path.join(DESKTOP, 'EXEMPLO')
NEW_FOLDER = os.path.join(DESKTOP, 'NEW_FOLDER')

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.copytree(MAIN_FOLDER, NEW_FOLDER)
shutil.move(NEW_FOLDER, NEW_FOLDER + '_NOVA')