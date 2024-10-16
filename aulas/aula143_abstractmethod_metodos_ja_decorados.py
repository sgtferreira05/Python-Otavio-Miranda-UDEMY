# abstractmethod para qualquer método já decorado
# É possível criar @property @property.setter @classmethod @staticmethod e métodos normais como abstratos, para isso use @abstractmethod como decorador mais interno.
# Foo - Bar : são palavras usadas como placeholders para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

# ABSTRACT COM O PROPERTY

# class AbstractFoo(ABC):
#     def __init__(self, name):
#         self._name = None
#         self.name = name


#     @property
#     @abstractmethod
#     def name(self):...



# class Foo(AbstractFoo):
#     def __init__(self, name):
#         super().__init__(name)
#         # print('Sou inútil')

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         self._name = name
    
# foo = Foo('Bar')
# print(foo.name)

# ABSTRACT COM SETTER

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name


    @property
    def name(self):
        return self._name
    
    
    @name.setter
    @abstractmethod
    def name(self, name):...



class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name
    
foo = Foo('Bar')
print(foo.name)