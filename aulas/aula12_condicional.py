# if / elif / else

entrada = input('Você quer "entrar" ou "sair"? ')
if  entrada == 'entrar':
    print('Você entrou no sistema')
    print('Seja bem vindo!')
elif entrada == 'sair':
    print('Você saiu do sistema')
    print('Muito obrigado!')
else:
    ...
print('Fora do bloco.')

condicao = False
if condicao:
    print('Este é o código do if')
else:
    print('')

if 10 == 10:
    print('Outro if')
print('Fora do código')