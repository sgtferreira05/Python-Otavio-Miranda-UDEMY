'''
enumerate -> enumera iteráveis (índices)
'''

lista = ['Maria', 'Curie', 'Helena']
lista.append('Vitória')

'''lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)'''


'''lista_enumerada = list(enumerate(lista, start=10))
print(lista_enumerada)'''

'''for item in enumerate(lista):
    print(item)'''


'''for indice, nome in enumerate(lista):
#    indice, nome = item
    print(indice, nome)'''


for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

