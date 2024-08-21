# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'
    def __init__(self, nome):
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)

    # def acao(self):
    #     # print(variavel)
    #     ...

# leao = Animal(nome='Leão')
# print(leao.nome)
# # print(leao.acao())
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('Maçã'))