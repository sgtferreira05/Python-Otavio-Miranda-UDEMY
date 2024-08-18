# Generator expression, Iterables and Iterators in Python

#   GENERATOR => SÃO FUNCOES QUE SABEM PAUSAR
import sys


'''iterable = ['I', 'Have', '__iter__']
iterator =  iter(iterable) #iterable.__iter__() 
# tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))

lista = [n for n in range(100000)]
generator = (n for n in range(100000))
             
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)
#for n in generator:
#    print(n)'''

###########################################

'''def generator(n=0):
    yield 'Seja bem vindo ao sistema' # Pausar
    yield 'Agora iremos coletar seus dados bancários' # 
    yield 'Confirme apertando o as teclas 1[OK] 2[ERRO]'

gen = generator(n=0)
print(next(gen))

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
print(next(gen))
conta = input('Digite o nº da conta: ')
agencia = input('Digite o nº da agencia: ')
print(next(gen))
print (f'NOME = {nome}\n'
      f'IDADE = {idade}\n'
      f'CONTA = {conta}\n'
      f'AGÊNCIA = {agencia}\n')

confirmacao = input('CONFIRMAÇÃO [0]/[1]: ')

##############################################
'''

'''def generator(n=0, maximum=10):
    while True:
        yield n
        if n == maximum:
            return
        n += 1

gen = generator(n=5, maximum=50)
for n in gen:
    print(n)'''

############################################
def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen):
    yield from gen()
    yield 10
    yield 20
    yield 30
    print('------------------')

def gen3():
    yield 100
    yield 200
    yield 300

g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
