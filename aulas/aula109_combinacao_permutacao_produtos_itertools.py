# Combinations, Permutations and Products - Itertools
#COMBINAÇÃO: Ordem não importa - ITERÁVEL + tamanho do grupo
#PERMUTAÇÃO: Ordem importa
#PRODUTO: Ordem importa e repete valores únicos

from itertools import combinations, permutations, product
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['Masculino', 'Feminino'],
    ['Infantil', 'Adulto'],
    ['Algodão', 'Seda'],
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')

# print_iter(combinations(pessoas, 2))
# print()
# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))