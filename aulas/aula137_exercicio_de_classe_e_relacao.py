# Exercício com classes
# 1. Crie uma classe Carro (Nome)
# 2. Crie uma classe Motor (Nome)
# 3. Crie uma classe Fabricante (Nome)
# 4. Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros.
# 5. Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros.
# 6. Exiba o nome do carro, motor e fabricante na tela.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
       
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

hb20 = Carro('HB20')
Hyundai = Fabricante('Hyundai')
motor_1_0 = Motor('1.0')
hb20.fabricante = Hyundai
hb20.motor = motor_1_0


fusca = Carro('Fusca')
volkswagem = Fabricante('VW')
fusca.fabricante = volkswagem
fusca.motor = motor_1_0

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0

print(hb20.nome, ' - ', hb20.fabricante.nome, ' - ', hb20.motor.nome)
print(fusca.nome, ' - ', fusca.fabricante.nome, ' - ', fusca.motor.nome)
print(fiat_uno.nome, ' - ', fiat_uno.fabricante.nome, ' - ', fiat_uno.motor.nome)

