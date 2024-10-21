#__new__ e __init__ em classes Python
#__new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
#__new__ : DEVE RETORNAR o novo objeto.

#__init__ é o método responsável por inicializar a instância. Por isso, init recebe self.
#__init__ : NÃO DEVE RETORNAR nada (None)

# object é a super classe de uma classe

class A:

    def __new__(cls, *args, **kwrgs):
        print('before creating the instance')
        instance = super().__new__(cls)
        print('after creating the instance')
        return instance

    def __init__(self, x):
        self.x = x
        print("I'm init")

    def __repr__(self):
        return 'A()'


a = A(125)
print(a.x)