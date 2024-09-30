# Relações entre classes: associação, agregação e composição.
# 1.    Associação: é um tipo de relação onde os objetos estão ligados dentro do sistema. Esta é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem um atributo que referência outro objeto.
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo...'

escritor = Escritor('Eça')
caneta = FerramentaDeEscrever('Caneta pena')
maquina_de_escrever = FerramentaDeEscrever('Máquina de escrever')
# escritor.ferramenta = caneta
escritor.ferramenta = maquina_de_escrever


print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())