'''
for in com listas
'''
from time import sleep
'''
from time import sleep
lista = ['Maria', 'Helena', 'Luiz', 'Creuza']
pos = 0
for nome in lista:
    print(pos, nome, type(nome))
    sleep(0.8)
    pos += 1
'''

lista = ['Creuza', 'Maria', 'Ellen', 'Edna', 'Je', 'Gabi']
indices = range(len(lista))

for indice in indices:
    print(indice,lista[indice], type(lista[indice]))
    sleep(0.8)