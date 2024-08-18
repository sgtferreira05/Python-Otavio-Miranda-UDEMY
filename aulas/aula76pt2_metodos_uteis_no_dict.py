'''
Métodos úteis os cidionários em Python

# len - quantas chaves;
# keys - iterável com as chaves;
# values - iterável com os valores;
# items - iterável com chaves e valores;
# setdefault - adiciona valor se a chave não existe;
# copy - retorna uma cópia rasa (shallow copy);
# get - obtém uma chave;
# pop - Apaga um item com a chave especificada (del);
# popitem - Apaga o último item adicionado; e
# update - Atualiza um dicionário com outro.
'''

pessoa = {
    'nome': 'Ailton',
    'sobrenome' : 'Ferreira1',
    'sobrenome' : 'Ferreira2',
    'sobrenome' : 'Ferreira',
    #'idade': 900,
}

# print(pessoa.__len__())
print(len(pessoa)) #Qtd de chaves
print()

# print(pessoa.keys())
print(list(pessoa.keys())) #retorna as chaves
for chave in pessoa.keys():
    print(chave)
print()

print(list(pessoa.values())) #retorna os valores
for valor in pessoa.values():
    print(valor)
print()

print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

print()

pessoa.setdefault('idade', None)
print(pessoa['idade'])
print()


