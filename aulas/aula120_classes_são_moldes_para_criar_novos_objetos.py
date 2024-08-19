# class - Classes são moldes para criar novos objetos.
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos (funções).
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.

# string = 'Ailton'   #str (class)
# print(string.upper())
# print(isinstance(string, str))

# CriarBaseDeDados = (PascalCase)
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa ('Ailton', 'Ferreira') #objeto
# p1.nome = "Ailton" #atributo
# p1.sobrenome = "Ferreira" #atributo


p2 = Pessoa ('Maria', 'Joana')
# p2.nome = "Maria"
# p2.sobrenome = "Joana"

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)