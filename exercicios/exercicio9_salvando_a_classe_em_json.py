# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos. Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'exercicio9_dados_salvos.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Ailton', 27)
p2 = Pessoa('Yuri', 7)
p3 = Pessoa('Maria', 52)
bd = [vars(p1), vars(p2), p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
