def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

# Com a função soma:
print(soma(2,3))
#ou
print(executa(soma, 2,3))
print()

#Com a função lambda
print(
    executa(
        lambda x, y: x + y, 2, 3
    )
)


print()
print()



def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador 
    return multiplica

#duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: m * n, 2
)
print(duplica(6))


#Exemplo extra
print()
print(
    executa(
        lambda *args: sum(args), 1,2,3,4,5,6,7
    )
)
