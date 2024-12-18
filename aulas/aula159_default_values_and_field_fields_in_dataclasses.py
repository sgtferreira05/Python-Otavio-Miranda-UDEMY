# Default values and field in dataclasses

from dataclasses import dataclass, field, fields

@dataclass
class Person:
    name: str = field(
        default='MISSING', repr=False
    )
    last_name: str = 'Not sent'
    age: int = 100
    adress: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Person()
    print(fields(p1))
    print(p1)