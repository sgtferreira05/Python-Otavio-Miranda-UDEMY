'''
            REPETIÇÕES
    > while (enquanto)
executa uma ação enquanto uma condição for verdadeira
'''


'''condicao = True
while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')
    if nome =='Ferreira':
        break
'''

'''from time import sleep
contador = 0

while contador <= 10:
    
    print(contador)
    sleep(0.3)
    contador += 1
print('ACABOU!')'''


             #       CONTINUE

'''
contador = 0

while contador <= 50:
    contador += 1

    if contador % 3 == 0:
        print(f'O número {contador} é divisível por 3')        
        continue

    if contador > 10 and contador < 15:
        print(f'Não vou mostrar o {contador}')
    print(contador)'''

                #   WHILE DENTRO DE WHILE

'''qtd_linhas = 5
qtd_colunas = 5
linha = 1

while linha <= qtd_linhas:
    colunas = 1
    while colunas <= qtd_colunas:
        print(f'{linha=} {colunas=}')
        colunas += 1
    linha += 1'''

                #   ITERANDO STRINGS COM WHILE

nome = "Ailton Ferreira"        #Iteráveis
tamanho_nome = len(nome)
cond = 0
novo_nome = ''

while cond < tamanho_nome:
    letra = nome[cond]
    novo_nome += f'*{letra}'
    cond += 1
print(novo_nome)




