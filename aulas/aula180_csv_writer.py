# csv.writer and csv.DictWriter
# csv.writer writes the CSV in a list format
# csv.DictWriter writes the CSV in a dictionary format

import csv
from pathlib import Path

WAY_CSV = Path(__file__).parent / 'aula180.csv'



# primeira forma:

# clients_list = [
#     {'Name': 'Ailton F Silva', 'Adress': 'R Pde, 221'},
#     {'Name': 'Stev F Silva', 'Adress': 'R Julio M, 1'},
#     {'Name': 'Ellen F Silva', 'Adress': 'R de l, 101'},
# ]

# with open(WAY_CSV, 'w') as file:
#     columns_names = clients_list[0].keys()
#     writer_ = csv.writer(file)

#     writer_.writerow(columns_names)

#     for client in clients_list:
#         writer_.writerow(client.values())

# 2 forma, mais hardcode

# lista_clientes = [
#     ['Ailton F', 'Av1, 22'],
#     ['Stev F', 'Av2, "1"'],
#     ['Ellen F', 'Av3, 3A'],
# ]
# with open(WAY_CSV, 'w') as arquivo:
#     nome_colunas = ['nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)

# 3 forma com dicionarios:

clients_list = [
    {'Name': 'Ailton F Silva', 'Adress': 'R Pde, 221'},
    {'Name': 'Stev F Silva', 'Adress': 'R Julio M, 1'},
    {'Name': 'Ellen F Silva', 'Adress': 'R de l, 101'},
]
with open(WAY_CSV, 'w') as file:
    columns_names = clients_list[0].keys()
    writer_ = csv.DictWriter(
        file,
        fieldnames=columns_names
    )
    writer_.writeheader()

    for client in clients_list:
        writer_.writerow(client)