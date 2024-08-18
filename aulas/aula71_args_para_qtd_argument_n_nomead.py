'''
args - Argumentos não nomeados
*- *args (empacotamento e desempacotamentos
'''

#   desempacotamento
#x, y, *resto = 1,2,3,4
#print(x,y,resto)

#def soma(x,y):
#    return x + y

def soma(*args):
    total = 0
#    args = list(args)
#    print(args, type(args))
    for numero in args:
#        print('Total:',total, numero)

        total += numero
#        print('Total:',total)
    return total
#soma(1,2,3,4,5,6)

soma_1_2_3 = soma(1,2,3)
#print(soma_1_2_3)

#print(outra_soma)

print(sum((2,3,4,64,5,1,3))) #Acontece sem erro
#print(sum(1,2,4,6,3,12,32,12)) #ERRO!! precisa desempacotar.

numeros = 1,2,4,6,4,21,22,42,1
outra_soma = soma(*numeros) #precisa desempacotar ( com * )
print(outra_soma)
print(numeros)

