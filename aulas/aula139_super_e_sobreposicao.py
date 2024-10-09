# Super() é a super class na sub class
# Class pricipal (Pessoa)
#   -> super class, base class, parent class
# Class filhas (Cliente)
#   -> sub class, child class, derived class



###############################

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         # return 'ABC'
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Ailton')
# print(string.upper())

###############################

class A:
    atributo_a = 'valor a'
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo,outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('Burlei o sistema!!')

    def metodo(self):
        # super(B,self).metodo() = B.metodo(self)
        A.metodo(self)
        print('C')


# print(C.mro()) #METHOD RESOLUTION ORDER DE C
# print(B.mro()) #METHOD RESOLUTION ORDER DE B
# print(A.mro()) #METHOD RESOLUTION ORDER DE A



c = C('atributo', 'qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()