# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# @property é uma ropriedade do objeto, ela é um método que se comporta como um atributo.   (??????????)
# Geralmente é usada nas seguintes situações:
# - p/ evitar quebrar código cliente;
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


#1       método que compromete os clientes

class Caneta:
    def __init__(self, cor):
        # private protected public
        self.cor = cor

#            Código cliente
caneta = Caneta('Verde')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)



#2       método com o getter
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor #posso mudar o nome do atributo
        
    def get_cor(self):
        return self.cor_tinta
    
#       Código cliente
caneta = Caneta('Verde')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())


#3       método com @property       
class Caneta:
    def __init__(self, cor):
        self.cor_tampa = cor #posso mudar o nome do atributo
    
    @property
    def cor(self):
        return self.cor_tampa
    
    @property
    def cor_atual(self):
        return 12345
    
#       Código cliente
caneta = Caneta('Verde')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_atual)