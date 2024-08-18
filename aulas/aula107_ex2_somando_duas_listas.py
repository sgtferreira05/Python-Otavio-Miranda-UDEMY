"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

=========== resultado
lista_soma = [2, 4, 6, 8]
"""


        #MINHA SOLUÇÃO
# lista_a = [1990, 1991, 1993, 1994, 1996]
# lista_b = [5, 9, 17, 22, 31, 51, 17, 19, 25]
# lista_soma = []


# lena = len(lista_a)
# lenb = len(lista_b)
# if lena <= lenb:
#     indice_min = lena
# else:
#     indice_min = lenb

# for i in range(0, indice_min - 1):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


        #SOLUÇÃO 1

# lista_a = [1990, 1991, 1993, 1994, 1996, 1997, 1999, 2000, 2007]
# lista_b = [5, 9, 17, 22, 31, 51]

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


        #SOLUÇÃO 2 ==== melhor forma

lista_a = [1990, 1991, 1993, 1994, 1996, 1997, 1999, 2000, 2007]
lista_b = [5, 9, 17, 22, 31, 51]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)