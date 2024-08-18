'''
split e join -> são usados com list e str
    split -> divide uma string
    join -> une uma string
'''

frase = 'Olha só que, coisa interessante'
'''# Separar a frase em palavras numa lista
lista_palavras = frase.split()
print(lista_palavras)'''


'''# Separar o periodo em frases usando o parâmetro ',' como parametro
lista_frases = frase.split(',')
print(lista_frases)'''


'''lista_frases = frase.split(',')
for i, frase in enumerate(lista_frases):
    #Strip corta os espaços do i e do f.
    #   rstrip -> corta os espaços da direita;
    #   lstrip -> corta os espaços da esquerda
    print(lista_frases[i].strip()) '''


frase1 = '    Olha só que  ,  coisa interessante     '
lista_frases_cruas = frase1.split(',')

lista_frases = []
for i, frase1 in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

'''print(lista_frases)
print(lista_frases_cruas)'''

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)