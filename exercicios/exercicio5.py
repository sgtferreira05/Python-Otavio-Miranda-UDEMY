'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não igite um número
inteiro, informe que não é um número inteiro.
'''

'''
num = input('Digite um número inteiro: ')
if num.isdigit():
    num_int = int(num)
    if num_int % 2 == 0:
        print('O número digitado é par.')
    else:
        print('O número digitado é ímpar.')
else:
    print('O número digitado não é um número inteiro.')



entrada = input('Digite um número: ')
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

'''




'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horarário
descrito, exiba a saudação apropriada.
'''


'''entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'Bom dia!! São {hora} horas da manhã.')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde! São {hora} horas da tarde.')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite! São {hora} horas da noite.')
    else:
        print('Hora inválida.')
except:
    print('Número digitado não é inteiro.')
'''





'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos, escreva 'Seu nome é curto'. Se tiver entre 5 e 6,
escreva 'Seu nome é normal'. Senão escreva 'Seu nome é muito grande'.
'''
nome = input('Digite seu primeiro nome: ')
qtd = len(nome)

if qtd > 1 :
    if qtd <= 4 :
        print('Seu nome é curto.')
    elif qtd <= 6 :
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite mais de 1 caractere !!!')
    
    








