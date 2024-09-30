class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento (self):
        return Pessoa.ano_atual - self.idade
    


dados = {'nome': 'Yuri', 'idade': 7}
p1 = Pessoa(**dados)
# p1 = Pessoa('Yuri', 7)
# p1.nome='Ailton'
# print(p1.idade)
# del p1.nome
# p1.__dict__['outra'] = 'coisa'
# print(p1.__dict__)
print(vars(p1))
print(p1.nome)


