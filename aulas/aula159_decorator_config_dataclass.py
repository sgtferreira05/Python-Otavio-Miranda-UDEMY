from dataclasses import dataclass


# @dataclass(frozen=True)
# class Person:
#     name: str
#     last_name: str

# if __name__ == '__main__':
#     p1 = Person('Ailton', 'Ferrera')
#     p1.name = 'Maria'
#     print(p1)

#############################
# @dataclass(repr=False)
# class Person:
#     name: str
#     last_name: str

# if __name__ == '__main__':
#     p1 = Person('Ailton', 'Ferrera')
#     print(p1)

###########################

# @dataclass(order=True)
# class Person:
#     name: str
#     last_name: str

# if __name__ == '__main__':
#     list = [Person('A', 'Z'), Person('B', 'Y'), Person('C', 'X')]
#     order = sorted(list, reverse=True)
#     print(order)

#######################

@dataclass
class Person:
    name: str
    last_name: str

if __name__ == '__main__':
    list = [Person('Maria', 'Fátima'), Person('Maria', 'Graça'), Person('Maria', 'Conceição')]
    order = sorted(list, reverse=False, key=lambda p: p.last_name)
    print(order)