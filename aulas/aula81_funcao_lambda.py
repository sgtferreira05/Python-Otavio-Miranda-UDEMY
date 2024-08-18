'''
Função lambda em Python:
A função lambda é uma função como qualquer outra em Python. Porém, são funções ANÔNIMAS que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
'''

lista = [
    {'nome': 'Luiz', 'sobrenome':'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel','sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#lista = [4,5,2,5,985,254,56,552,145,4789,622,1]
#lista.sort(reverse=True)
#print(lista)



def ordena(item):
    #return item['nome']
    return item['sobrenome']

lista.sort(key=ordena) #Precisamos ensinar ao Python como ordenar dicionário
for item in lista:
    print(item)


# Com a função lambda e list
print()
print()

lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)

# Com a função lambda, def e sorted
print()
print()    

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

