# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
# Assinatura de método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais SO'L'ID
# Princípio da substituição de Liskov:
#Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = 👎
# Sobreposição de métodos (override) 🐍 = 👍

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: #Type anotation
        ...
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False

# n = NotificacaoEmail('Testando notificação')
# n.enviar()
# n = NotificacaoSMS('Testando notificação')
# n.enviar()

def notificar(notificacao:Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao não enviada')

notificar(NotificacaoEmail('Testando e-mail'))
notificar(NotificacaoSMS('Testando SMS'))


