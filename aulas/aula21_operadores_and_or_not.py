#       Operadores Lógicos
# and (e) or (ou) not (não)

'''
 and - Todas as condições precisam ser verdadeiras.
 São considerados falsy : 0, 0.0, '', False
 Também existe o tipo None que é usado para represen-
tar um não valor.
'''

'''
or - Qualquer condição verdadeira avalia toda a expressão
como verdadeira.
'''

'''
not - Usado para inverter expressões:
    not True = False
    not False = True
'''



#   OPERADOR AND
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Aqui estão seus dados: ')
else:
    print('Saindo do sistema...')


print(True and False and True)
print(True and 0 and True)
'''

#   OPERADOR OR
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Aqui estão seus dados: ')
else:
    print('Saindo do sistema...')
   

print(0 or False or 0 or 'abc' or True)
senha = input('Senha: ') or 'Sem senha'
print(senha)
'''

#   Operador NOT
'''
senha = input('Senha: ')
if not senha:
    print('Você não digitou nada.')

print(not 1)
print(not 0)
'''
