# Relações entre classes: associação, agregação e composição.
# 2.    Agregação: é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
# Geralmente, é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa. (Existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            # self._produtos.append(produto)
            # self.produtos += produtos
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

 
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco



carrinho = Carrinho()
p1, p2 = Produto('Headphones', 117), Produto('MousePad', 79)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())