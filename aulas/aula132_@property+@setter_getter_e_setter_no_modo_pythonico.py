# @property + @setter - getter e setter no modo pythônico
# - como getter:
# p/ evitar quebrar código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# atributos que começar com um ou dois underlines NÃO devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor
        self._cor_tampa = None

#       método para obter o valor(getter)
    @property
    def cor(self):
        return self._cor
#       método para configurar o valor(setter)
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
    




caneta = Caneta('Verde')
caneta.cor = 'Pink'
print(caneta.cor)
caneta.cor_tampa = 'Branco'
print(caneta.cor_tampa)