# gruoupby -> agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Teodorico', 'nota': 'C'},
    {'nome': 'Rubião', 'nota': 'D'},
    {'nome': 'Quincas Borba', 'nota': 'B'},
    {'nome': 'Bentinho', 'nota': 'B'},
    {'nome': 'Iracema', 'nota': 'A'},
]

def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena )
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)



