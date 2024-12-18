from dataclasses import dataclass, asdict, astuple

@dataclass
class Person:
    name: str
    last_name: str

if __name__ == '__main__':
    p1 = Person('Ailton', 'Ferrera')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])