'''
-   Dicionários em Python ( tipo dict)
Dicionários são estruturas de dados do tipo par de 'chave' e 'valor'

Chaves: podem ser consideradas como o 'índice' que vimos na lista e podem ser de tipos imutáveis como : str, int, float, bool, tuple, etc.

Valor: pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.

Imutáveis: str, int, float, bool, tuple...
Mutáveis: dict, list

Exemplos:
'''

# pessoa = dict(nome='Luiz Otavio', sobrenome= 'Miranda')

pessoa = {
    'nome': 'Ailton',
    'sobrenome': 'Ferreira',
    'idade': 27,
    'altura': 1.8,
    'enderecos': [
        { 'rua': 'Dr Pena', 'numero': 123},
        { 'rua': 'Julio Mario', 'numero': 321}      
    ],
}
#print(pessoa, type(pessoa))
#for chave in pessoa:
    #print(chave, ': ',pessoa[chave])





######################################################

# Manipulando chaves e valores em dicionários
    
people = {}

people['nome'] = 'Ailton F' #Criar chaves
print(people)
print(people['nome'])

chave = 'nome_completo'
people[chave] = 'Ailton Ferreira da Silva'
print(people[chave])
print(people)

del people['nome'] #Apagar chaves
print(people)

if people.get('nome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['nome'])