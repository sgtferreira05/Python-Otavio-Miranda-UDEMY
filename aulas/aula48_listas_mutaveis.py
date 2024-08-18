'''
Listas em Python
Tipo list - Mutável
Suportar vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create - Read - Update - Delete = lista[i] (CRUD)
'''

#      +01234
#      -54321

'''lista = [123, True, 'Ailton F Silva', 1.2, []]
lista[-3] = 'Maria de Fátima'
print(lista)
print(lista[2], type(lista[2]))'''


lista = [10,20,30,40,50]

#       DELETE

'''lista[2] = 400
print(lista)
print(lista[2])
del lista[2]
print(lista)
print(lista[2])'''

#       ADICIONANDO, APPEND

'''lista.append(60)
lista.append(70)
lista.append(80)
print(lista)'''

#       REMOVENDO, POP

'''lista.append(60)
lista.pop()
lista.append(70)
lista.append(80)
ultimo_valor = lista.pop()
print(lista, 'Removido: ', ultimo_valor)
lista.pop(1)
print(lista)'''

#       LIMPAR, .clear()

'''lista.clear()
print(lista)'''

#       INSERIR NUM DETERMINADO LUGAR, .insert()
# obs.: o método insert recebe dois argumentos(posição, valor)


'''lista.append('Luiz')
print(lista)
lista.append(1233)
del lista[-1]
print(lista)
lista.insert(0,5)
print(lista)'''

#       CONCATENANDO COM + OU .extend():

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b 
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

