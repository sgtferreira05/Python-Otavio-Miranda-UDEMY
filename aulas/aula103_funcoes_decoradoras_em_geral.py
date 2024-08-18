# Funções decoradoras e decoradores

# Decorar = Adicionar / Remover / Restringir / Alterar
# funções decoradoras são funções que decoram outras funções

# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são 'Syntax Sugar' (Açucar sintático)



# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Iniciando decorador...')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}')
#         print('OK, agora o resultado está decorado em nosso BD')
#         return resultado
#     return interna


# def inverte_string(string):
#     return string[::-1]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError ('Param deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)


# invertida = inverte_string_checando_parametro('Ailton')
# print(invertida)


# DECORADOR  SYNTAX SUGAR 

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('OK, agora você foi decorada')
        return resultado
    return interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError ('Param deve ser um string')

@criar_funcao #Syntax Sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

invertida = inverte_string('123')
print(invertida)