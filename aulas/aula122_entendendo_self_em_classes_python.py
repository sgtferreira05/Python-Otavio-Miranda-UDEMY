# Entendendo self em classes Python
# Classe - Molde (Geralmente, sem dados)
# Instância da class (object) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome='sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')




fusca = Carro('Fusca')
fusca.acelerar()
# Carro.acelerar() cookie de natal, não da para comer o molde
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()
