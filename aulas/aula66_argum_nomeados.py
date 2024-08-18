'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado - tem o nome com sinal de igual
Argumento não nomeado - recebe apenas o argumento (valor)
'''

def soma(x, y):
    #definição
    print(f'{x=} + y={y}', '|', 'x + y = ', x + y )

soma(1, 2)
soma(y=3, x=2)



def somaa(x, y, z):
    print(f'{x=} + {y=} + {z=}', '|', 'x + y + z = ', x + y + z)
somaa(2,5,z=4)


print(1,2,4, sep='-')