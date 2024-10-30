# Decorator function and method-based decorators



def add_rpr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def internal(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Earth' in result:
            return "You're at home"
        return result
    return internal

@add_rpr
class Team:
    def __init__(self, name):
        self.name = name
@add_rpr
class Planet:
    def __init__(self, name):
        self.name = name
    @my_planet
    def say_name(self):
        return f'{self.name} planet'


brazil = Team('Brazil')
portugal = Team('Portugal')
earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)
print(earth)
print(mars)
print(earth.say_name())
print(mars.say_name())