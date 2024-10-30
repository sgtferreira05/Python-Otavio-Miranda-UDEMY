# Decorator function and clas-based decorators

# First way
# class Team:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
# class Planet:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

# brazil = Team('Brazil')
# portugal = Team('Portugal')
# earth = Planet('Earth')
# mars = Planet('Mars')

# print(brazil)
# print(portugal)
# print(earth)
# print(mars)


# Second way (HERANÇA)
# class MyReprMixix:
# class Team(MyReprMixix):
#     def __init__(self, name):
#         self.name = name

# class Planet(MyReprMixix):
#     def __init__(self, name):
#         self.name = name

# brazil = Team('Brazil')
# portugal = Team('Portugal')
# earth = Planet('Earth')
# mars = Planet('Mars')

# print(brazil)
# print(portugal)
# print(earth)
# print(mars)


# Third way (COMPOSITION)
def add_rpr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls
@add_rpr
class Team:
    def __init__(self, name):
        self.name = name
@add_rpr
class Planet:
    def __init__(self, name):
        self.name = name


brazil = Team('Brazil')
portugal = Team('Portugal')
earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)
print(earth)
print(mars)