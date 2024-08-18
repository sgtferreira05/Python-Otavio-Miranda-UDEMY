# Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador: ', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='fiveth')
@parametros_decorador(nome='fourth')
@parametros_decorador(nome='third')
@parametros_decorador(nome='second')
@parametros_decorador(nome='first')
def soma(x,y):
    return x+y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)