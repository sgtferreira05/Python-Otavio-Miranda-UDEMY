# Herança simples - Relações entre classes.
# Associação > Usa;
# Agregação > tem;
# Composição > é dono de; e
# Herança > é um

# Herança vs Composição

# Classe principal (Pessoa)
#   ->super class, base class, parent class

# Classes filhas (Clientes)
#   -> sub class, child class, derived class

# Method resolution order(MRO): é a ordem que o python vai buscar as funções, para saber qual é a MRO, basta entrar na help da classe e verificar.

        # Super class
class Pessoa:
    cpf = '11111'
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    def falar_nome_classe(self):
        print(self.prenom, self.nom, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Nem saí da classe CLIENTE')
        print(self.prenom, self.nom, self.__class__.__name__)


class Aprovados(Pessoa):
    cpf = '33333'

c1 = Cliente('Ailton', 'F')
c1.falar_nome_classe()
apv = Aprovados('Ailton', 'Ferreira')
apv.falar_nome_classe()
print(apv.cpf)
# help(Cliente)