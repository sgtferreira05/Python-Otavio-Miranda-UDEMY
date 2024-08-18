# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/reference/datamodel.html
# inteiro - import nome_modulo
# vantagens: você tem o namespace do módulo
# desvantagens: nomes grandes

'''import sys
platform = 'A MINHA'
print(sys.platform)
sys.exit()
'''

# partes - from nome_modulo import objeto1, objeto2
# vantagens: nomes pequenos
# desvantagens: Sem o namespace do módulo

'''from sys import exit, platform
print(platform)'''

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modulo import objeto as apelido
# vantagens: você pode reservar nomes para seu código
# desvantagens: pode ficar fora do padrão da linguegem

'''import sys as s
sys = 'alguma coisa'
print(s.platform)
print(sys)'''

'''from sys import platform as pf, exit as ex

print(pf)
print(ex)
'''
# na prática - from nome_modulo import *
# vantagens: importa tudo de um módulo
# desvantagens: importa tudo de um módulo

from sys import *
print(platform)
exit()