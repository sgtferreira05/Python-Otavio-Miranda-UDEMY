
import accounts

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age: int):
        self._age = age
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'

class Customer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None

if __name__ == '__main__':
    c1 = Customer('Aifes', 28)
    c1.account = accounts.CheckingAccount(1278, 156582, 2300, 1500)
    print(c1)
    print(c1.account)
    print()
    c1 = Customer('Maria', 52)
    c1.account = accounts.SavingAccount(1278, 156583, 2500)
    print(c1)
    print(c1.account)