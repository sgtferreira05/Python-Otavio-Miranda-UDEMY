# Classes abastratas - Abstract Base Class (abc)
# Abcs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos. Também podem ter métodos concretos por elas mesmas.
# @abastractmethods são métodos que não têm corpo. As regras para classes abastratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.
# Métodos abastratos DEVEM ser implementados nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.
# É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod
# from abc import ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta):
class Log(ABC):
    @abstractmethod
    def _log(self, msg):...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('Oi')

