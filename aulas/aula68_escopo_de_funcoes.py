#Aula 68
'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir;
Existe o escopo global e o local;
ESCOPO GLOBAL:
    É o escopo onde todo o código é alcançável.
ESCOPO LOCAL:
    É o escopo onde apenas nomes do mesmo local podem ser alcançados.
'''

'''x = 4 #Escopo global
def escopo():
    global x
    x = 10
    def outra_funcao():
        global x
        x = 7
        y = 2
        print(x, y)
 #   x = 1 #Escopo local
    print(x)
    outra_funcao()
print(x)
escopo()
print(x)
'''

# Aula 69
'''
NÃO temos acesso a nomes de escopos internos nos escopos externos;
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno;
'''

x = 1

def escopo():
    global x
    x = 10
    
    def outra_funcao():
        global x
        y = 1
        x = 11
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)