# Encapsulamento (modificadores de acesso: public, protected e private)
# Python NÃO TEM modificadores de acesso, mas podemos seguir as seguintes convenções:
# 1.    (SEM UNDERLINE) = public, pode ser usado em qualquer lugar;
# 2.    (UM UNDERLINE) = protected, NÃO DEVE ser usado fora da classe ou suas subclasses;
# 3.    (DOIS UNDERLINES) = private, 'NAME MANGLING'(desfiguração de nomes) em Python só DEVEE ser usado na classe em que foi declarado.

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é privado'
    
    def metodo_publico(self):
        print(self.__exemplo)
        return 'metodo_publico'
    
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'




f = Foo()
print(f.public)
print(f.metodo_publico())


# print(f._protected)
# print(f._metodo_protected())


# print(f.__exemplo)