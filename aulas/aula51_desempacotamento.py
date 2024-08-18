'''
Introdução ao desempacotamento + tuples (tuplas)
'''


'''nome1, nome2, nome3 = ['Creuza', 'Maria', 'Ellen']
print(nome2)
'''

#ERR0 -> Muitos valores para desempacotar:
'''nome1, nome2 = ['Edna', 'Je', 'Gabi']
print(nome1)'''


#ERRO -> Poucos valores para desempacotar:
'''nome1, nome2, nome3 = ['Creuza', 'Maria']
print(nome1)'''

#CERTO -> Colocar um asterisco para identificar os demais vlores:
#Usa o _ para classificar os nomes, não será utilizado.
nome1, *_ = ['Maria', 'Creuza', 'Ellen', 'Edna', 'Jenn', 'Gabi']
print(nome1)

_, nome2, *_ = ['Maria', 'Creuza', 'Ellen', 'Edna', 'Jenn', 'Gabi']
print(nome2)

_, _, nome3, *_ = ['Maria', 'Creuza', 'Ellen', 'Edna', 'Jenn', 'Gabi']
print(nome3)
