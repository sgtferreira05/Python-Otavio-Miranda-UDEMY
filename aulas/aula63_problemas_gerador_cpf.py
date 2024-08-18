        

        # Alterando os caracteres especiais:
'''cpf_enviado_usuario = '420.457.558-78' \
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')\

print(cpf_enviado_usuario)

import re
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    '420.45dasdasdas     adasdasd   adadadasdas7.558-78'
)
print(cpf_enviado_usuario)'''

import re

entrada = input('CPF: ')
cpf_maquina = re.sub(
    r'[^0-9]',
    '',
    entrada
)

print(entrada)
print(cpf_maquina)

        # Verificando se o valor é sequencial

import sys

entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()
