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

################################
'''import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1' : [0, 1, 2],
}'''

# Copia rasa

'''
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)'''


# deepcopy

'''d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)
'''
####################################


p1 = {
    'nome': 'Luiz',
    'sobrenome' : 'Miranda',
}

# ---> get

#print(p1['nome'])
#print(p1.get('nome', 'Não existe'))

# --> pop

#nome = p1.pop('nome')
#print(nome)
#print(p1)

# --> popitem

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

# --> update

p1.update({
    'nome': 'novo_valor',
    'idade': 30,
})

p1.update(nome='novo valor', altura=1.8)

tupla =(('nome', 'new values'),('peso', 74))
p1.update(tupla)

lista = [['nome', 'Ailton'], ['sexo','masculino']]
p1.update(lista)

lista

print(p1)

