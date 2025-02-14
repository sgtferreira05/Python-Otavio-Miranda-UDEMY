# os + shutil - move, copy and delete files
# move/rename -> shutil.move
# move/rename -> os.rename
# copy -> shutil.copy
# delete -> os.unlink
# delete directory recursively -> shutil.rmtree
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
print(HOME)
print(DESKTOP)