# dir, hasattr and getattr in Python

string = 'Ailton'
metodo = 'upper'


if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)