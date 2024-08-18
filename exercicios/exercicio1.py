nome = str(input('Escreva o nome: '))
sobrenome = str(input('Escreva o sobrenome: '))
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = int(input('Informe a sua idade: '))
maior_de_idade = idade >= 18
altura_metros = float(input('Informe a sua altura em metros: '))

print('REGISTRO DE MORADOR')
print('NOME: ', nome)
print('SOBRENOME: ', sobrenome)
print('IDADE: ', idade)
print('ANO DE NASCIMENTO: ', ano_de_nascimento)
print('MAIOR DE IDADE? ', maior_de_idade)
print('ALTURA:', altura_metros, 'm')