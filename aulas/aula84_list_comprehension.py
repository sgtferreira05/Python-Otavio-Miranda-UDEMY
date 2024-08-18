import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir
# de iteráveis.

#print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

    # List comprehension:

'''lista = [numero for numero in range(10)]
print(lista)
lista1 = [numero * 3 for numero in range(10)]
print(lista1)
lista2 = [numero - 1 for numero in range(10)]
print(lista2)'''

#   Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
#print(novos_produtos)
#print(*novos_produtos, sep='\n')


#   Filtro em list comprehension

lista = [n for n in range(10) if n %2 != 0]
#p(lista) 

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos 
    if produto['preco'] > 10
]
p(novos_produtos)



