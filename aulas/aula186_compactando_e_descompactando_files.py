# ZIP - Compressing and decompressing files with zipfile.ZipFile

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Paths
ROOT_PATH = Path(__file__).parent
DIR_ZIP_PATH = ROOT_PATH / 'aula_186_directory_zip'
COMPACTED_PATH = ROOT_PATH / 'aula_186_compacted.zip'
DESCOMPACTED_PATH = ROOT_PATH / 'aula_186_descompacted'

shutil.rmtree(DIR_ZIP_PATH, ignore_errors=True)
Path.unlink(COMPACTED_PATH, missing_ok=True)
shutil.rmtree(str(COMPACTED_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(DESCOMPACTED_PATH, ignore_errors=True)


# Raise Exception()

# Create a directory
DIR_ZIP_PATH.mkdir(exist_ok=True)

def create_files(qtd: int, dir_zip: Path):
    for i in range(qtd):
        text = 'file_%s' % i
        with open(dir_zip / f'{text}.txt', 'w') as f:
            f.write(text)
            f.write('\n')

create_files(10, DIR_ZIP_PATH)

# Create a zip file and add files to it
with ZipFile(COMPACTED_PATH, 'w') as zip:
    for root, dirs, files in os.walk(DIR_ZIP_PATH):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Reading the zip file
with ZipFile(COMPACTED_PATH, 'r') as zip:
    for file in zip.namelist():
        print(file)

# Extracting the zip file
with ZipFile(COMPACTED_PATH, 'r') as zip:
    zip.extractall(DESCOMPACTED_PATH)