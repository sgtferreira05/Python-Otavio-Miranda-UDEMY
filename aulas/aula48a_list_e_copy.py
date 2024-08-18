'''
Cuidado com dados mutáveis

    = -> copiado o valor (imutáveis)
    = -> aponta para o mesmo valor na memória (mutável)
'''

# Dessa maneira, estou fazendo a var b apontar para a mesma var a,
#portanto, se eu alterar qalq uma das listas, estarei mudando as duas.

'''
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)
'''

#Dessa maneira, estou criando outro espaço na memória com os mesmos
#valores de a para b. portanto, se eu alterar a, não estarei alterando
#nada em b e vice-versa.
#  -> .copy()

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
