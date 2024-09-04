# Métodos de classe:
#São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)
    
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p4 = Pessoa.criar_sem_nome(50)

print(p2.nome, p2.idade)
print(p1.nome, p1.idade)
print(p4.nome, p4.idade)



    