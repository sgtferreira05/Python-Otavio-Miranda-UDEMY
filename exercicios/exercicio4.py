'''
Exercício
Peça ao usuário para digitar nome e idade.
Em seguida, exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Caso o usuário não digitar nada de entrada, exiba:
    ''Desculpe, você deixou campos vazios.
'''

nome = (input('Escreva seu nome: '))
idade = int(input('Escreva a sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome};')
    print(f'Seu nome invertido é {nome[::-1]};')
    if ' ' in nome:
        print(f'Seu nome contém  espaços;')
    else:
        print('Seu nome não contém espaços;')
    print(f'Seu nome tem {len(nome)} caracteres;')
    print(f'A primeira letra do seu nome é {nome[0]}; e')
    print(f'A última letra do seu nome é {nome[-1]}.')
else:
    print('Desculpe, você deixou campos vazios.')


