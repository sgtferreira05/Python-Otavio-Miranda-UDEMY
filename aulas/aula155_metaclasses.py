# Metaclasses are the type of classes.
# IN PYTHON, EVERYTHING IS AN OBJECT (INCLUDING CLASSES)
# So, what is the type of a class? (Type)
# Your object is an instance of its class.
# Your class is an instance of type (type is a metaclass)
# type('Name', (Bases,), __dict__)
# 
# When creating a class, things happen by default in this order:
# __new__from metaclass is called and creates the new class
# __call__ from metaclass is invoked with arguments and calls:
#   __new__ from class with arguments (creates the instance)
#   __init__ from class with arguments
# __call__ from metaclass finishes the execution


    # Essential metaclass methods
# __new__ (mcs, name, bases, dct) (creat the class)
# __call__ (cls, *args, **kwargs) (creat and start the instance)

#"Metaclasses are deeper magic than 99% of users need to worry about. If you're wondering if you need them, you probably don't. (People who really need them know for sure that they need them and don't need an explanation why")
# -Tim Peters (CPython Core Developer)


# --------------------------------------------------------
# # object upper
# # class Foo():
# #     ...

# Foo = type('Foo', (object,), {}) # the second way to creat a class

# f = Foo()
# print(isinstance(f, Foo))
# print(type(f))
# print(type(Foo))
# ---------------------------------------------------------

from typing import Any


def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Metaclass New')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        if 'tlk' not in cls.__dict__ or not callable(cls.__dict__['tlk']):
            raise NotImplementedError('Implement tlk')
        return cls
    

    def __call__(self, *args, **kwargs):
        instance = super().__call__(*args,**kwargs)
        if 'name' not in instance.__dict__:
            raise NotImplementedError('Implement attr name')        

        return instance

class People(object, metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('My new')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print('My init')
        self.name = name

    def tlk(self):
        print('talking...')
    

p1 = People('Ailton')
# print(p1.attr)
# print(People.attr)
p1.tlk()