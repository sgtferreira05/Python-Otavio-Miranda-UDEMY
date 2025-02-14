# ps.path.getsize and os.stat to file's datas
import math
import os
from itertools import count

os.system('cls')

def  format_file_size(size_in_bytes: int, base: int = 1024) -> str:
    """Format a size in bytes to apropriete size"""
    # If the size is lower or equal 0, 0B.
    if size_in_bytes <= 0:
        return "OB"
    # Tuples with the sizes
    #                      0     1     2    3      4     5
    sizes_abbreviations = "B", "KB", "MB", "GB", "TB", "PB"
    # math.log will return the logarithm of size_in_bytes
    # With the base (1024 by default) this should match our index in the size abbreviation.
    index_abb_size = int(math.log(size_in_bytes, base))
    # By what factor should we divide our size to get the correct size
    power = base ** index_abb_size
    # Our final size
    final_size = round(size_in_bytes / power, 2)
    # The abbreviation that we want
    size_abbreviation = sizes_abbreviations[index_abb_size]
    return f'{final_size} {size_abbreviation}'


path = os.path.join("\\CURSOS", "python_udemy", "EXEMPLO")
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'CURRENT PASTA', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR:', dir_)
    
    for file_ in files:
        complete_file_way = os.path.join(root, file_)
        # size = os.path.getsize(complete_file_way)
            # second way:
        stats = os.stat(complete_file_way)
        size = stats.st_size
        print(' ', the_counter, 'FILE:', file_, format_file_size(size))



