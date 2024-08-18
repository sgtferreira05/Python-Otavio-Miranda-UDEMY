# Exercicios com funções

'''Crie uma função que multiplica todos os argumentos não nomeados recebidos e retorne o total para uma variável e mostre o valor da variável.'''




def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

valores = 1,5,4,3,2,1,6,5
resultado = multiplicador(*valores)
print(resultado)




'''Crie uma função, fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.'''

def identifier(x):
    if x % 2 == 0:
        return f'{x} is Even'
    return f'{x} is Odd'

print(identifier(12))
print(identifier(25))
print(identifier(33))
print(identifier(25))

