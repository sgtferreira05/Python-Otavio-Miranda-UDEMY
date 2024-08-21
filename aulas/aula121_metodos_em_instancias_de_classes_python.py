# Métodos em instâncias de classes Python
# Hard coded é algo que foi escrito diretamente no código.

class Carro:
    def __init__(self, nome='sei lá'):
        # fusca.nome = 'Fusca'           # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')




fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
