'''
Python = Linguagem de programação
Tipo de tipagem = Dinâmica (Python ja sabe qual tipo do dado)/ Forte
str = String (Texto)
'''
print(1234) #Python ja sabe que isso é int, não precisa informar.

#Não há diferença entre aspas simples e duplas
    # Aspas simples
print('Ailton Ferreira')
    # Aspas duplas
print("Ailton Ferreira")
    # Escape
print("Ailton \"Ferreira") # O \ não vai ler o proximo caracter como função(serve para escrever aspas nos textos)
    # r
print(r"Ailton \"Ferreira\"") #o r serve para mostrar o caracter de escape
    # Melhor solução para colocar aspas:
print('Ailton "Ferreira')


    # Tipo de dado bool (boolean)
# Ao questionar algo em um programa, so existem duas respostas possíveis:
# - Sim (True) ou Não (False).

# Existem vários operadores para 'questionar', dentre eles:
# - (==) questiona se um valor é igual ao outro;
# - (!=) questiona se um valor é diferente do outro;
# - (>,<) questiona se um valor é maior ou menor, respectivamente, a um outro;
# - etc.

print(10==10) #Sim => True
print(10==8) #Não => False
print(1>2) #Não => False
print(type(10==10)) #classe: bool
