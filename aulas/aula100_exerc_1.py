import copy
from dados import produtos
# Exercícios

# 1.
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)
]
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()


# 2.
# Ordene os produtos por nome decrescente
# Gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()

# 3.
# Ordene os produtos por preco crescente
# Gere produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda pr: pr['preco']
)
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')

