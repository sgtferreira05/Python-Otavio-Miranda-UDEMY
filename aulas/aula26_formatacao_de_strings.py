'''
Formatação básica de strings
s -> strings
d -> inteiro
f -> float
. <número de dígitos>f
x ou X -> Hexadecimal
(Caractere)(><^)(quantidade)
> -> Esquerda
< -> Direita
^ -> Centro
Sinal -> + ou -

Ex.: 0 > 100, .1f
Conversion flags -> !r !s !a
'''

var = 'ABC'
print(f'{var}')
print(f'{var:->10}.')
print(f'{var:-<10}.')
print(f'{var:-^10}.')
print(f'{10003.9031203910:+,.3f}')
print(f'O hexadecimal de 29 é {1500:X}')


