import accounts, person

class Bank:
    def __init__(
            self,
            branchs:list[int] | None = None,
            customers:list[person.Person] | None = None,
            accounts:list[accounts.Account] | None = None,
        ):
        self.branchs = branchs or []
        self.customers = customers or []
        self.accounts = accounts or []

    def _checking_branch(self, account):
        if account.branch in self.branchs:
            print('_checking_branch', True)
            return True
        print('_cheking_branch', False)
        return False
        
    def _checking_customer(self, customer):
        if customer in self.customers:
            print('_checking customer', True)
            return True
        print('_checking_customer', False)
        return False
        
    def _checking_account(self, account):
        if account in self.accounts:
            print('_checking account', True)
            return True
        print('checking_account', False)
        return False
    
    def _checking_if_account_from_customer(self, customer, account):
        if account is customer.account:
            print('_checking_if_account_from_customer', True)
            return True
        print('_checking_if_account_from_customer', False)
        return False

    def authenticate(self, customer:person.Person, account:accounts.Account):
        return self._checking_branch(account) and \
            self._checking_customer(customer) and \
            self._checking_account(account) and \
            self._checking_if_account_from_customer(customer, account)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branchs!r}, {self.customers!r},{self.accounts!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1 = person.Customer('Aifes', 28)
    ca1 = accounts.CheckingAccount(1278, 15690, 2300, 1500)
    c1.account = ca1
    c2 = person.Customer('Maria', 52)
    sa1 = accounts.SavingAccount(1278, 15691, 2500)
    c2.account = sa1 
    bank = Bank()
    bank.customers.extend([c1, c2])
    bank.accounts.extend([ca1, sa1])
    bank.branchs.extend([111, 222, 1278])



if bank.authenticate(c1, ca1):
    ca1.withdraw(108)
    ca1.withdraw(108)
    ca1.withdraw(108)
    ca1.withdraw(108)
    ca1.withdraw(108)
    ca1.deposit(270)
    ca1.deposit(360)
    ca1.deposit(270)
    ca1.deposit(270)
    ca1.deposit(270)
    print(c1.account)