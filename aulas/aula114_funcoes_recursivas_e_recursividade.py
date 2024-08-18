# Funções recursivas e recursividades
#   - funções que podem se chamar de voltar
#   - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
#   - Um problema que possa ser dividido em partes menores
#   - Um caso recursivo que resolve o pequeno problema
#   - Um caso base que para a recursão
# #   - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
# import sys 
# sys.setrecursionlimit(1005)


# def recursiva(inicio=0, fim=4):
#     print(inicio, fim)
#     #Caso base:
#     if inicio >= fim:
#         return fim
#     #Caso recursivo: contar até chegar no fim
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1000))

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Número: '))
print(f'{n}! = ', factorial(n))