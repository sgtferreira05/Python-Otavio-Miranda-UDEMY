'''
            Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será
usado.
'''

def soma(x, y, z=None):
    #CORRETO
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
    #ERRADO
    '''if z = 0:
        print(f'...')
    else:
        print(...)
    '''
    
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(1, 9, 0)