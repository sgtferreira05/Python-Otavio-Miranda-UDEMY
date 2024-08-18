nome = str(input('Nome: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura ** 2)
situacao = ''
if imc < 17:
    situacao = 'MUITO ABAIXO DO PESO'
elif 17 <= imc < 18.49:
    situacao = 'ABAIXO DO PESO'
elif 18.49 <= imc < 24.99:
    situacao = 'PESO NORMAL'
elif 24.99 <= imc < 29.99:
    situacao = 'ACIMA DO PESO'
elif 29.99 <= imc < 34.99:
    situacao = 'OBESIDADE 1'
elif 34.99 <= imc < 39.99:
    situacao = 'OBESIDADE 2(severa)'
else:
    situacao = 'OBESIDADE 3(mórbida)'

print('-=' * 15)
print('Cálculo do IMC')
print('-=' * 15)
print(f'{nome} tem {altura:.2f}m, pesa {peso:.2f}KG e seu IMC é {imc:.2f}')
print(f'Situação {situacao}')

