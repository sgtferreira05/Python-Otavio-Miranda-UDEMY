# os.walk
# os.walk is a function that recursively a directory structure.
# It generates a sequence of tuples, each containing three elements: The current directory (root), a list of subdirectories(dirs) and a list of files in the current directory(files).

import os
from itertools import count

path = os.path.join("\\CURSOS", "python_udemy", "EXEMPLO")
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'CURRENT PASTA', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR:', dir_)
    
    for file_ in files:
        complete_file_way = os.path.join(root, file_)
        print(' ', the_counter, 'FILE:', complete_file_way)

