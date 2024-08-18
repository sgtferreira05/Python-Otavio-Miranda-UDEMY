'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permitir que o programa quebre com
erros de índices inexistentes na lista.
'''
import os

lista_compras = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar \n')
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)
    elif opcao == 'a':
        indice = input('Escolha o índice para apagar: ')
        
        try:
            indice_str = int(indice)
            del lista_compras[indice_str]

        except ValueError:
            print('Por favor, digite número int.')
        
        except IndexError:
            print('índice não existe na lista')

    elif opcao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Nada a listar')
        else:
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
    else:
        print('Opção inválida')


    