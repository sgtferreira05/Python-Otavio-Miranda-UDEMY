'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
'''

import decimal
#numero_1 = 0.1
#numero_2 = 0.7

#Recomenda-se usá-los como str somente para somas sem precisão
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')

numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') #Retorna o valor em forma de str
print(round(numero_3, 2)) #Retorna o valor vdd que é float
