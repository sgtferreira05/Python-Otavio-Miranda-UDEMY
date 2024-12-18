from dataclasses import dataclass

@dataclass
class Person:
    name: str
    last_name: str

    def __post_init__(self):
        self.full_name = f'{self.name} {self.last_name}'


if __name__ == '__main__':
    p1 = Person('Ailton', 'Ferrera')
    print(p1)
    print(p1.full_name)
