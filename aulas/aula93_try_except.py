# Try, except, else e finally

'''a = 18
b = 0
c = a / b #SILENCIANDO UM ERRO
'''
try:
    ...
    a = 18
    b = 0
    print(a/b)
    print(b[0])
    print('Linha 1')
    c = a/b #SILENCIANDO UM ERRO
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Name not defined')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('NAME:', error.__class__.__name__)

except Exception: #Exception é o erro superior do python
    print('UNKNOWN ERROR')

print('CONTINUAR')