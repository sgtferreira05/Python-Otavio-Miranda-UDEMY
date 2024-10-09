# Herança Múltipla - Python Orientado a Objetos
# quer dizer que no python, uma classe pode estender várias outras classes.

# Herança Simples:
#   Animal-> Mamífero -> Humano -> Pessoa -> Cliente

# Herança Múltipla e mixins:
    # Log -> FileLog
#   Animal-> Mamífero -> Humano -> Pessoa -> Cliente
        # Cliente(Pessoa, FileLog)

# Python3 usa C3 superclass linearization para gerar o mro.
# Para saber a ordem de chamada de métodos use o método de classe 
# Classe.mro() ou o atributo __mro__

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    def quem_sou(self):
        print('B')

class C:
    ...

    # def quem_sou(self):
    #     print('C')

class D(C, B):
    ...

    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou()
print(D.mro())