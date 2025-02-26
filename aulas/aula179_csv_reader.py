# csv.reader and csv.DictReader
# csv.reader reads the CSV in a list format
# csv.DictReader reads the CSV in a dictionary format
import csv
from pathlib import Path

CSV_WAY = Path(__file__).parent / 'aula179.csv'

with open(CSV_WAY, 'r') as file:
    reader = csv.DictReader(file)
    # next(reader) #pular a primeira linha

    for line in reader:
        print(line)
        print(line['NOME'], line['IDADE'], line['ENDERECO'])



# with open(CSV_WAY, 'r') as file:
#     reader = csv.reader(file)
#     # next(reader) #pular a primeira linha

#     for line in reader:
#         print(line)