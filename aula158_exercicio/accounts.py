import abc

class Account(abc.ABC):
    def __init__(self, branch:int, accountNumber:int, balance:float=0)->None:
        self.branch = branch
        self.accoutNumber = accountNumber
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, amount:float) -> float:
        self.amount = amount

    def deposit(self, amount: float) -> float:
        self.balance += amount
        self.details(f'(Deposit US${amount})')
        return self.balance

    def details(self, msg: str='')->None:
        print(f'Balance: US${self.balance:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r}, {self.accoutNumber!r}, {self.balance!r})'
        return f'{class_name}{attrs}'

class SavingAccount(Account):
    def withdraw(self, amount):
        balance_after_withdraw = self.balance - amount

        if balance_after_withdraw >= 0:
            self.balance -= amount
            self.details(f'(WITHDRAW U${amount})')
            return self.balance
        print('The requested withdrawal amount was not available')
        self.details(f'\nDENIED WITHDRAW {amount}')
        return self.balance



class CheckingAccount(Account):
    def __init__(self, branch:int, accountNumber:int, balance:float=0, limit:float=0):
        super().__init__(branch, accountNumber, balance)
        self.limit = limit

    def withdraw(self, amount:float) ->float:
        balance_after_withdraw = self.balance - amount
        cap = -self.limit

        if balance_after_withdraw >= cap:
            self.balance -= amount
            self.details(f'(WITHDRAW US${amount})')
            return self.balance
        print('The requested withdrawal amount was not available')
        print(f'Your cap is: US${-self.limit:.2f}')
        self.details(f'\nDENIED WITHDRAW US${amount:.2f}')
        return self.balance

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r}, {self.accoutNumber!r}, {self.balance!r}, {self.limit!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    sa1 = SavingAccount(1278, 665874, 715.27)
    sa1.withdraw(17.28)
    sa1.deposit(270)
    sa1.withdraw(136.79)
    print('\n##')
    ca1 = CheckingAccount(1272, 156984, 4841.62, 1000)
    ca1.withdraw(1112.28)
    ca1.deposit(700)
    ca1.withdraw(1316.79)
    ca1.withdraw(3161.79)
    ca1.withdraw(900)

