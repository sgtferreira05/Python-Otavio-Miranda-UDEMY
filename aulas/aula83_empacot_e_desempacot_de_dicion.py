# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

#print(a,b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome': 'Souza',
}
#------
#a, b = pessoa
#a, b = pessoa.values()
#a, b = pessoa.items()

#print(a,b)
#-------


'''
(a1,a2), (b1,b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
'''
#-------

dados_pessoa = {
    'idade': 16,
    'altura': 1.79,
}

pessoa_completa = {**pessoa, **dados_pessoa}

#print(pessoa_completa)
#-------



    #args e kwargs 
#args -> Argumentos não nomeados
#kwargs -> keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
#mostro_argumentos_nomeados(**pessoa_completa)
        
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)