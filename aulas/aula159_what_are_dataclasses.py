# Dataclasses - What are dataclasses?
# The dataclasses module provide a decorator and functions to create methods like __init__(), __repr__(), __eq__(),..., for user-defined classes.
# summary: dataclasses are syntax sugar to create normal classes.
# It was specified in PEP 557 and added in 3.7 Python version.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    last_name: str

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'
    
    @full_name.setter
    def full_name(self, value):
        name, *last_name = value.split()
        self.name = name
        self.last_name = ' '.join(last_name)

if __name__ == '__main__':
    p1 = Person('Ailton', 'Ferrera')
    p1.full_name = 'Maria de Fátima'
    print(p1.full_name)


